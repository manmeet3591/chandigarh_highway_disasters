import requests
import os

# Chandigarh Study Area Bounding Box
# Format: (south, west, north, east)
BBOX = "30.35,75.85,30.90,76.90"

OVERPASS_URL = "http://overpass-api.de/api/interpreter"

def fetch_highways():
    """
    Fetches highway geometries within the bounding box using Overpass API.
    """
    query = f"""
    [out:json][timeout:25];
    (
      way["highway"~"motorway|trunk|primary|secondary"]({BBOX});
    );
    out body;
    >;
    out skel qt;
    """
    
    headers = {
        'User-Agent': 'CHD-HDD-Project/1.0 (manmeet.singh@example.com)',
        'Accept': 'application/json'
    }
    
    print(f"Fetching highway data for BBOX: {BBOX}...")
    try:
        response = requests.get(OVERPASS_URL, params={'data': query}, headers=headers)
        response.raise_for_status()
        
        os.makedirs('data/raw', exist_ok=True)
        file_path = 'data/raw/chandigarh_highways.json'
        with open(file_path, 'w') as f:
            f.write(response.text)
        print(f"Successfully saved highway data to {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        if response is not None:
            print(response.text)


if __name__ == "__main__":
    fetch_highways()
