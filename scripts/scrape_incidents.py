import requests
from bs4 import BeautifulSoup
import json
import os
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_chandigarh_section():
    """
    Scrapes the main Chandigarh news section of The Tribune.
    """
    url = "https://www.tribuneindia.com/news/chandigarh/"
    print(f"Scraping Chandigarh news section: {url}")
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []
        
        # Selectors identified from research
        for card in soup.select('.story-card, .story-box, .news-list-item'):
            title_tag = card.select_one('h2.title, h3.title, .title')
            link_tag = card.select_one('a')
            date_tag = card.select_one('.time, .date')
            summary_tag = card.select_one('.description, p')
            
            if title_tag and link_tag:
                title_text = title_tag.get_text(strip=True)
                summary_text = summary_tag.get_text(strip=True) if summary_tag else ""
                
                # Check for disaster keywords in title or summary
                disaster_keywords = ["accident", "mishap", "injured", "highway", "collision", "pile-up", "landslide", "cave-in", "flooding", "truck"]
                is_disaster = any(kw in title_text.lower() or kw in summary_text.lower() for kw in disaster_keywords)
                
                if is_disaster:
                    url = link_tag.get('href')
                    if url and not url.startswith('http'):
                        url = "https://www.tribuneindia.com" + url
                        
                    articles.append({
                        "title": title_text,
                        "url": url,
                        "date": date_tag.get_text(strip=True) if date_tag else "Unknown",
                        "summary": summary_text
                    })
        
        print(f"  Found {len(articles)} disaster-related leads in the Chandigarh section.")
        return articles

    except Exception as e:
        print(f"  Error scraping Chandigarh section: {e}")
        return []

def main():
    leads = scrape_chandigarh_section()
    
    os.makedirs('data/raw', exist_ok=True)
    output_path = 'data/raw/news_incident_leads.json'
    with open(output_path, 'w') as f:
        json.dump(leads, f, indent=2)
    
    print(f"\nScraping complete. Total leads saved: {len(leads)}")
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    main()
