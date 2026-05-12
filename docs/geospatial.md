# Geospatial Definition: Chandigarh Study Area

This document defines the geospatial "box" around Chandigarh used for highway disaster analysis.

## Bounding Box Coordinates
The study area is defined by the following WGS84 coordinates:

- **North (Max Lat):** 30.90
- **South (Min Lat):** 30.35
- **West (Min Lon):** 75.85
- **East (Max Lon):** 76.90

### Coordinates Summary
- **Top-Left (NW):** `(30.90, 75.85)`
- **Bottom-Right (SE):** `(30.35, 76.90)`

## Key Highways in Scope
- **NH5:** Major highway passing through Zirakpur and Chandigarh, connecting towards Shimla.
- **NH44:** Key artery passing near Ambala (South of the box) and Ludhiana (West of the box).
- **State Highways:** Various Chandigarh and Punjab/Haryana state highways within the box.

## Methodology
Data collection scripts (e.g., `scripts/fetch_osm_data.py`) will use these coordinates to filter incidents and infrastructure data.
