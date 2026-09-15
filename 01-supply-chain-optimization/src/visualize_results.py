"""
Supply Chain Optimization Case
Visualization Script
Author: Juan C Lopez A.
Description: Generates executive charts for the Supply Chain case study,
             including Fill Rate, Capacity vs. Demand, and Inventory Coverage.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_visuals(data_path, output_dir):
    """
    Loads analyzed data and generates executive visualizations.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Load the analyzed dataset
    df = pd.read_csv(data_path)
    
    # Set a professional style
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # 1. Chart: Fill Rate by Warehouse
    plt.figure(figsize=(10, 6))
    fill_rate = df.groupby('Warehouse')['Fill_Rate'].mean().reset_index()
    plt.bar(fill_rate['Warehouse'], fill_rate['Fill_Rate'], color='#2E86AB')
    plt.axhline(y=0.95, color='r', linestyle='--', label='Target (95%)')
    plt.title('Average Fill Rate by Warehouse', fontsize=14, fontweight='bold')
    plt.ylabel('Fill Rate (%)')
    plt.xlabel('Warehouse')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/fill_rate_by_warehouse.png")
    plt.close()
    
    # 2. Chart: Demand vs. Production Capacity (Top 10 records)
    plt.figure(figsize=(12, 6))
    sample = df.head(20)
    x = range(len(sample))
    plt.bar(x, sample['Demand'], width=0.4, label='Demand', color='#A23B72')
    plt.bar([i + 0.4 for i in x], sample['Production_Capacity'], width=0.4, label='Capacity', color='#F18F01')
    plt.title('Demand vs. Production Capacity (Sample)', fontsize=14, fontweight='bold')
    plt.ylabel('Units')
    plt.xlabel('Record Index')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/demand_vs_capacity.png")
    plt.close()
    
    # 3. Chart: Inventory Coverage Days by SKU
    plt.figure(figsize=(10, 6))
    inv_coverage = df.groupby('SKU')['Inventory_Coverage_Days'].mean().reset_index()
    plt.plot(inv_coverage['SKU'], inv_coverage['Inventory_Coverage_Days'], marker='o', color='#3B1F2B', linewidth=2)
    plt.title('Average Inventory Coverage Days by SKU', fontsize=14, fontweight='bold')
    plt.ylabel('Days of Coverage')
    plt.xlabel('SKU')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/inventory_coverage.png")
    plt.close()
    
    print(f"Visualizations generated successfully in {output_dir}/")

if __name__ == "__main__":
    print("Generating Supply Chain visualizations...")
    
    # Paths
    analyzed_data_path = "../data/supply_chain_analyzed.csv"
    output_directory = "../reports/figures"
    
    try:
        generate_visuals(analyzed_data_path, output_directory)
    except FileNotFoundError:
        print(f"Error: Analyzed dataset not found at {analyzed_data_path}. Please run analyze_supply_chain.py first.")
