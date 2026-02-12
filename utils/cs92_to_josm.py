# -*- coding: utf-8 -*-
import json
from pyproj import Transformer

INPUT = "input.geojson"
OUTPUT = "output_crs84.geojson"

# EPSG:2177 to CRS84 (lon, lat)
transformer = Transformer.from_crs(
    "EPSG:2177",
    "OGC:CRS84",
    always_xy=True
)

# Rough Poland bounding box (sanity check)
POLAND_BBOX = {
    "lon_min": 14.0,
    "lon_max": 25.0,
    "lat_min": 49.0,
    "lat_max": 55.5,
}

def in_poland(lon, lat):
    return (
        POLAND_BBOX["lon_min"] <= lon <= POLAND_BBOX["lon_max"]
        and POLAND_BBOX["lat_min"] <= lat <= POLAND_BBOX["lat_max"]
    )

def transform_coords(coords):
    # Point
    if isinstance(coords[0], (int, float)):
        x, y = coords[:2]  # drop Z
        lon, lat = transformer.transform(x, y)

        if not in_poland(lon, lat):
            raise ValueError(
                f"Reprojection failed: ({lon:.6f}, {lat:.6f}) outside Poland"
            )

        return [lon, lat]

    # LineString / Polygon / Multi*
    return [transform_coords(c) for c in coords]

with open(INPUT, "r", encoding="utf-8") as f:
    data = json.load(f)

for feature in data.get("features", []):
    geom = feature.get("geometry")
    if geom and "coordinates" in geom:
        geom["coordinates"] = transform_coords(geom["coordinates"])

# GeoJSON RFC 7946: no CRS member
data.pop("crs", None)

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("? Conversion successful output is JOSM-compatible and in Poland.")
