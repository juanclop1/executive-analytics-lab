"""
Supply Chain Optimization Case
Analysis & KPI Calculation Script
Author: Juan C Lopez A.
Description: Reads the synthetic supply chain data and calculates key performance
             indicators (KPIs) for executive decision-making.
"""

import pandas as pd
import numpy as np

def calculate_kpis(file_path):
    """
    Loads data and calculates strategic supply chain KPIs.
    """
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # 1. Fill Rate (Percentage of committed demand fulfilled)
    df['Fill_Rate'] = df['Actual_Delivery'] / df['Committed_Delivery']
    
    # 2. Capacity Utilization (Demand vs. Production Capacity)
    df['Capacity_Utilization'] = df['Demand'] / df['Production_Capacity']
    
    # 3. Inventory Coverage Days (Available Inventory / Daily Demand)
    # Assuming 30 days per period for simplicity
    df['Inventory_Coverage_Days'] = (df['Available_Inventory'] / (df['Demand'] / 30))
    
    # 4. Total Lead Time
    df['Total_Lead_Time'] = df['Supplier_Lead_Time_Days'] + df['Transport_Lead_Time_Days']
    
    # 5. Logistics Cost per Unit
    df['Logistics_Cost_Per_Unit'] = df['Logistics_Cost_USD'] / df['Actual_Delivery']
    
    # Aggregate KPIs by Warehouse
    summary = df.groupby('Warehouse').agg({
        'Fill_Rate': 'mean',
        'Capacity_Utilization': 'mean',
        'Inventory_Coverage_Days': 'mean',
        'Total_Lead_Time': 'mean',
        'Logistics_Cost_Per_Unit': 'mean'
    }).reset_index()
    
    return df, summary

if __name__ == "__main__":
    print("Starting Supply Chain Analysis...")
    
    # Path to the generated data
    data_path = "../data/supply_chain_data.csv"
    
    try:
        df_analyzed, summary_kpis = calculate_kpis(data_path)
        
        # Save the results
        df_analyzed.to_csv("../data/supply_chain_analyzed.csv", index=False)
        summary_kpis.to_csv("../data/supply_chain_kpi_summary.csv", index=False)
        
        print("Analysis complete. Results saved to data/ folder.")
        print("\nExecutive KPI Summary by Warehouse:")
        print(summary_kpis)
        
    except FileNotFoundError:
        print(f"Error: Dataset not found at {data_path}. Please run generate_data.py first.")
