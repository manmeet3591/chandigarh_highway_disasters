import geopandas as gpd
import matplotlib.pyplot as plt
import os

def visualize_network():
    print("Loading geospatial layers...")
    
    # Load Highway Network
    highways_path = 'data/processed/chandigarh_highways.geojson'
    blackspots_path = 'data/processed/chandigarh_blackspots.geojson'
    
    if not os.path.exists(highways_path) or not os.path.exists(blackspots_path):
        print("Required data files not found. Please run fetch_osm_data.py and process_geodata.py first.")
        return

    highways = gpd.read_file(highways_path)
    blackspots = gpd.read_file(blackspots_path)
    
    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Plot highways
    # Color by type for better visualization
    highways.plot(ax=ax, color='gray', linewidth=0.5, alpha=0.7, label='Road Network')
    
    # Highlight major highways (NH5/NH44) if tagged
    major_roads = highways[highways['ref'].isin(['NH5', 'NH 5', 'NH44', 'NH 44'])]
    if not major_roads.empty:
        major_roads.plot(ax=ax, color='blue', linewidth=1.5, label='National Highways (NH5/NH44)')
    
    # Plot Blackspots
    blackspots.plot(ax=ax, color='red', marker='o', markersize=50, label='Accident Blackspots', edgecolor='black', zorder=5)
    
    # Annotate Blackspots
    for x, y, label in zip(blackspots.geometry.x, blackspots.geometry.y, blackspots['name']):
        ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points", fontsize=8, fontweight='bold')


    plt.title('Chandigarh Highway Network & Disaster Blackspots', fontsize=15)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Save the visualization
    os.makedirs('visualizations', exist_ok=True)
    save_path = 'visualizations/chandigarh_disaster_map.png'
    plt.savefig(save_path, dpi=300)
    print(f"Visualization saved to {save_path}")

if __name__ == "__main__":
    visualize_network()
