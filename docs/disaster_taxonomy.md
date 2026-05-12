# Chandigarh Highway Disaster Taxonomy

This document classifies the types of disasters and hazards being tracked in the CHD-HDD project.

## 1. Weather-Induced Disasters
- **Fog-Related Pile-ups:** Large-scale multi-vehicle collisions occurring during dense winter fog (Visibility < 50m).
  - *Primary Locations:* NH44 (Ambala-Ludhiana), NH5 (Zirakpur-Kalka).
- **Monsoon Landslides & Washouts:** Destruction of highway sections due to heavy rain and slope failure.
  - *Primary Locations:* NH5 (Parwanoo-Shimla stretch near Chandigarh).
- **Urban Flash Flooding & Cave-ins:** Road collapses or submersions due to drainage failure during intense rainfall.
  - *Primary Locations:* Industrial Area, Sector-specific arterial roads.

## 2. Infrastructure & Traffic Hazards
- **Blackspot Collisions:** High-frequency fatal accident zones identified by Chandigarh Police.
  - *Key Spots:* Hallomajra, Poultry Farm Chowk, Kalagram Light Point.
- **Hazardous Material Spills:** Chemical or fuel leaks from tankers on the highway network.
- **Wrong-Side Driving Crashes:** Head-on collisions caused by vehicles using the wrong lane (common near unauthorized highway cuts).

## 3. Data Attributes to Track
For each incident in the dataset, we aim to capture:
- **Timestamp:** Date and time of the event.
- **Type:** (Landslide, Pile-up, Cave-in, etc.)
- **Location:** Lat/Lon coordinates and Highway Name.
- **Severity:** Number of fatalities/injuries, extent of infrastructure damage.
- **Contributing Factors:** Weather (Fog/Rain), Speeding, Design Flaw.
