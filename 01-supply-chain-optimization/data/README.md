# Data Governance & Structure - Supply Chain Optimization

## 📋 Purpose
This folder contains the synthetic data generated for the Supply Chain Optimization case study. The data is designed to simulate a complex international export program with multiple SKUs, warehouses, and logistical constraints.

## 🔐 Data Governance
To protect commercial confidentiality and adhere to ethical data practices, all data in this repository is **100% synthetic**. 
* No real client names, product specifications, or supplier data are included.
* No real transactional values, contracts, or negotiated prices are used.
* The data is generated programmatically using Python (`src/generate_data.py`) with a fixed random seed to ensure reproducibility.

## 📊 Data Dictionary
The dataset (`supply_chain_data.csv`) contains the following fields:

| Field | Description | Type |
| :--- | :--- | :--- |
| `Date` | Month of the record (YYYY-MM) | String |
| `SKU` | Product identifier | String |
| `Warehouse` | Distribution center identifier | String |
| `Demand` | Customer demand for the period | Integer |
| `Production_Capacity` | Available production capacity | Integer |
| `Available_Inventory` | Inventory available at the start of the period | Integer |
| `Supplier_Lead_Time_Days` | Days for supplier to deliver raw materials | Integer |
| `Transport_Lead_Time_Days` | Days for transportation to destination | Integer |
| `Unit_Cost_USD` | Cost per unit | Float |
| `Logistics_Cost_USD` | Total logistics cost for the period | Float |
| `Committed_Delivery` | Contractual delivery commitment | Integer |
| `Actual_Delivery` | Actual units delivered | Integer |

## ▶️ How to Reproduce
To generate the dataset and run the analysis, execute the following commands from the `src/` directory:
```bash
python generate_data.py
python analyze_supply_chain.py
python visualize_results.py
