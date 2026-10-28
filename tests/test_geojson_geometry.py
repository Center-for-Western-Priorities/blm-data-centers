"""Tests for how ArcGIS rings are turned into GeoJSON geometry.

ArcGIS returns one flat list of rings per case: clockwise rings are outer
boundaries (separate parts), counter-clockwise rings are holes. GeoJSON
instead nests holes under their shell, and any extra ring in a `Polygon`
is a hole. Writing every ring into one `Polygon` turned separate parts
into bogus "holes" outside their shell.

Needs shapely (requirements-dev.txt).
"""
import json
import os
import sys

import pytest
from shapely.geometry import Polygon, shape

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from add_geometry import rings_to_geojson_geometry  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def square(x, y, size, clockwise):
    """Closed ring for a size x size square at (x, y)."""
    ring = [[x, y], [x, y + size], [x + size, y + size], [x + size, y], [x, y]]  # clockwise
    return ring if clockwise else ring[::-1]


def signed_area(ring):
    return sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(ring, ring[1:])) / 2


def polygons_of(geom):
    return [geom["coordinates"]] if geom["type"] == "Polygon" else geom["coordinates"]


def test_single_ring_is_a_plain_polygon():
    geom = rings_to_geojson_geometry([square(0, 0, 10, clockwise=True)])
    assert geom["type"] == "Polygon"
    assert len(geom["coordinates"]) == 1


def test_separate_parts_become_a_multipolygon():
    rings = [square(0, 0, 10, True), square(20, 0, 10, True)]
    geom = rings_to_geojson_geometry(rings)
    assert geom["type"] == "MultiPolygon"
    assert [len(p) for p in geom["coordinates"]] == [1, 1]
    assert shape(geom).area == pytest.approx(200)


def test_hole_stays_under_its_shell():
    rings = [square(0, 0, 10, True), square(2, 2, 4, False)]
    geom = rings_to_geojson_geometry(rings)
    assert geom["type"] == "Polygon"
    assert len(geom["coordinates"]) == 2
    assert shape(geom).area == pytest.approx(100 - 16)


def test_hole_goes_to_the_shell_that_contains_it():
    rings = [square(0, 0, 10, True), square(20, 0, 10, True), square(22, 2, 4, False)]
    geom = rings_to_geojson_geometry(rings)
    assert geom["type"] == "MultiPolygon"
    ring_counts = sorted(len(p) for p in geom["coordinates"])
    assert ring_counts == [1, 2]
    with_hole = next(p for p in geom["coordinates"] if len(p) == 2)
    assert Polygon(with_hole[0]).bounds[0] == 20
    assert shape(geom).area == pytest.approx(100 + 100 - 16)


def test_winding_follows_rfc_7946():
    rings = [square(0, 0, 10, True), square(2, 2, 4, False)]
    shell, hole = rings_to_geojson_geometry(rings)["coordinates"]
    assert signed_area(shell) > 0   # exterior counter-clockwise
    assert signed_area(hole) < 0    # hole clockwise


def test_hole_outside_every_shell_is_an_error():
    rings = [square(0, 0, 10, True), square(50, 50, 4, False)]
    with pytest.raises(ValueError):
        rings_to_geojson_geometry(rings)


def test_every_published_hole_is_inside_its_shell():
    """A hole outside its shell is exactly what the old writer produced for
    multi-part cases. (Other validity quirks are not checked here: BLM's own
    Townsite polygon pinches at one point, and adjacent PLSS lots touch inside
    the Harquahala line and Jacqueline MultiPolygons.)
    """
    with open(os.path.join(ROOT, "data_center_row_cases.geojson")) as f:
        features = json.load(f)["features"]
    bad = []
    for feat in features:
        for poly in polygons_of(feat["geometry"]):
            shell = Polygon(poly[0]).buffer(0)
            if any(not shell.covers(Polygon(hole).buffer(0)) for hole in poly[1:]):
                bad.append(feat["properties"]["case_number"])
                break
    assert bad == []
