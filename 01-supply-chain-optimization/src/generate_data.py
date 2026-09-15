"""
Supply Chain Optimization Case
Synthetic Data Generator
Author: Juan C Lopez A.
Description: Generates a synthetic dataset representing an international export program
             with demand, production capacity, inventory, and lead times.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

def generate_supply_chain_data(periods=12, skus=5, warehouses=3):
    """
    Generates synthetic supply chain data.
    """
    dates = [datetime(2023, 1, 1) + timedelta(days=30*i) for i in range(periods)]
    
    data = []
    
    for date in dates:
        for sku in range(1, skus + 1):
            for wh in range(1, warehouses + 1):
                # Base demand with seasonality and noise
                base_demand = np.random.randint(500, 2000)
                seasonality = 1 + 0.2 * np.sin(2 * np.pi * date.month / 12)
                demand = int(base_demand * seasonality * np.random.uniform(0.8, 1.2))
                
                # Capacity and Inventory
                production_capacity = int(demand * np.random.uniform(0.9, 1.3))
                available_inventory = int(demand * np.random.uniform(0.5, 1.5))
                
                # Lead times (days)
                supplier_lead_time = np.random.randint(15, 45)
                transport_lead_time = np.random.randint(10, 30)
                
                # Costs
                unit_cost = round(np.random.uniform(50, 200), 2)
                logistics_cost = round(np.random.uniform(1000, 5000), 2)
                
                # Delivery commitments
                committed_delivery = int(demand * np.random.uniform(0.95, 1.05))
                actual_delivery = int(committed_delivery * np.random.uniform(0.85, 1.0))
                
                data.append({
                    'Date': date.strftime('%Y-%m'),
                    'SKU': f'SKU-{sku:03d}',
                    'Warehouse': f'WH-{wh:02d}',
                    'Demand': demand,
                    'Production_Capacity': production_capacity,
                    'Available_Inventory': available_inventory,
                    'Supplier_Lead_Time_Days': supplier_lead_time,
                    'Transport_Lead_Time_Days': transport_lead_time,
                    'Unit_Cost_USD': unit_cost,
                    'Logistics_Cost_USD': logistics_cost,
                    'Committed_Delivery': committed_delivery,
                    'Actual_Delivery': actual_delivery
                })
                
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    print("Generating synthetic Supply Chain data...")
    df = generate_supply_chain_data()
    
    # Save to CSV
    output_path = "../data/supply_chain_data.csv"
    df.to_csv(output_path, index=False)
    print(f"Data generated successfully: {output_path}")
    print(f"Total records: {len(df)}")
    print(df.head())
