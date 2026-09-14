# 1. Supply Chain Optimization Case

## 📋 Business Context
Design of a Supply Chain model to support an international export program of regulated industrial material to the Middle East, involving multiple supply constraints, lead times, logistics capacity, and contractual commitments. 

The main challenge was to coordinate demand, availability, production, documentation, transportation, and international deliveries to fulfill the program without generating contractual penalties.

## 📊 Data Used
This repository uses a combination of synthetic data and normalized parameters derived from a real professional case.
* Export program value: ~USD 37M.
* 120 international freight containers.
* Scheduled demand and deliveries by period.
* Production and dispatch capacity.
* Available inventory and requirements.
* Supplier and transportation lead times.
* Logistics costs.
* Storage capacity.
* Committed delivery dates.
* Supply risks and constraints.

*Note: To protect commercial information, client names, products, suppliers, routes, and individual transactional values are replaced with identifiers and synthetic data.*

## 🔧 Methodology
1. Consolidation of demand and delivery commitments.
2. Normalization of inventories, capacities, and lead times.
3. Identification of critical Supply Chain constraints.
4. Segmentation of materials by criticality and supply risk.
5. Calculation of inventory requirements and reorder points.
6. Capacity vs. demand analysis.
7. Construction of delay and recovery scenarios.
8. Simulation of different supply strategies.
9. Prioritization of orders according to financial and contractual impact.
10. Construction of an executive dashboard for program monitoring.

**Tools:** Python · Pandas · NumPy · Matplotlib · Jupyter Notebook · Excel · Power BI

## 📈 Findings
The model allows identifying:
* Bottlenecks before they affect committed dates.
* Materials whose shortage can halt an entire order.
* Financial exposure associated with delays.
* Required capacity per period.
* Differences between contractual demand and available capacity.
* Optimal logistics prioritization scenarios.

The analytical reconstruction demonstrates a simulated reduction in safety stock and an improvement in service level through a strategy based on criticality and demand variability.

## 📊 KPIs
| KPI | Objective |
| :--- | :--- |
| OTIF | Maximize delivery compliance |
| Fill Rate | Maximize availability |
| Inventory Days | Reduce tied-up capital |
| Lead Time | Minimize cycle time |
| Capacity Utilization | Optimize utilization |
| Logistics Cost / Unit | Control logistics cost |
| Contractual Exposure | Minimize penalty risk |
| Forecast Accuracy | Improve planning |

## ▶️ Reproduction Instructions
```bash
git clone <repository-url>
cd 01-supply-chain-optimization
pip install -r requirements.txt
jupyter notebook
