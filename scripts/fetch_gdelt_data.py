import pandas as pd
import requests
import os
import json

# Chandigarh Bounding Box
# lat_min, lat_max, lon_min, lon_max
BBOX = (30.35, 30.90, 75.85, 76.90)

def fetch_gdelt_events(query_keyword="disaster", limit=100):
    """
    Fetches events from GDELT 2.0 API within the Chandigarh region.
    Note: This uses the GDELT Doc API for searching news mentions with geographic filters.
    """
    print(f"Querying GDELT for '{query_keyword}' events in Chandigarh region...")
    
    # GDELT Doc API endpoint
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    
    params = {
        "query": f'"{query_keyword}" (location:"Chandigarh, India" OR location:"Zirakpur" OR location:"Panchkula" OR location:"Mohali")',
        "mode": "artlist",
        "format": "json",
        "maxrecords": limit
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if "articles" in data:
            articles = data["articles"]
            print(f"Found {len(articles)} relevant reports on GDELT.")
            
            os.makedirs('data/raw', exist_ok=True)
            with open(f'data/raw/gdelt_{query_keyword}_incidents.json', 'w') as f:
                json.dump(articles, f, indent=2)
            return articles
        else:
            print("No articles found for this query.")
            return []
            
    except Exception as e:
        print(f"Error querying GDELT: {e}")
        return []

import time

if __name__ == "__main__":
    # Combine keywords to reduce API calls
    query_str = '(pile-up OR landslide OR flooding OR accident)'
    fetch_gdelt_events(query_str, limit=250)
    
    print("GDELT fetch attempted with combined query.")


