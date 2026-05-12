# Chandigarh Highway Disaster Dataset (CHD-HDD)

This project aims to create a comprehensive dataset of highway disasters across a specific geospatial "box" around Chandigarh, India.

## Geospatial Scope
The study area encompasses Chandigarh, Mohali, Panchkula, and key stretches of **NH5** and **NH44**.

## Disaster Focus
The dataset tracks all major regional highway disasters, including:
- **Fog-Related Pile-ups:** Common during North Indian winters.
- **Monsoon Landslides & Washouts:** Particularly on the NH5 Himalayan gateway.
- **Urban Road Cave-ins:** Infrastructure failures during flash floods.
- **High-Fatality Blackspots:** Systematic mapping of deadly collision zones.

## Project Goal
To collect, clean, and structure data regarding these regional hazards to aid in research, predictive modeling, and safety improvements.



## Directory Structure
- `data/raw/`: Original, unmodified data files.
- `data/processed/`: Cleaned and structured datasets ready for analysis.
- `scripts/`: Python or shell scripts for data scraping, cleaning, and processing.
- `notebooks/`: Jupyter notebooks for exploratory data analysis (EDA).
- `docs/`: Documentation regarding data sources, methodology, and regional context.

## Planned Technologies
- **Python**: Primary language for data processing.
- **Pandas/NumPy**: For data manipulation.
- **Geopandas**: For geographic data analysis of Chandigarh highways.
- **BeautifulSoup/Scrapy**: If web scraping is required from news or traffic portals.

## Build and Run
- **Setup:** `pip install -r requirements.txt` (TODO: Create requirements file)
- **Data Collection:** `python scripts/collect_data.py` (TODO: Implement)
- **Data Processing:** `python scripts/process_data.py` (TODO: Implement)

## Development Conventions
- Document all data sources in `docs/sources.md`.
- Maintain a clear changelog for dataset versions.
- Follow PEP 8 for Python scripts.

