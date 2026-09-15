# 2. Business Performance Dashboard

## 📋 Business Context
Construction of an executive Business Performance system to transform scattered operational and financial information into actionable indicators for decision-making.

The objective is to connect financial results, operations, productivity, and compliance through an integrated KPI model.

## 📊 Data Used
Synthetic dataset built to represent an industrial organization with:
* Monthly sales.
* Direct and indirect costs.
* Gross margin.
* OPEX.
* EBITDA.
* Produced volume.
* Productivity.
* Inventories.
* Delivery compliance.
* Installed capacity.
* Headcount.
* Budget vs. Actuals.

Approximately 36 months of information are generated to allow for trend and seasonality analysis.

## 🔧 Methodology
1. Definition of the KPI tree.
2. Integration of financial and operational information.
3. Data cleaning and normalization.
4. Construction of profitability metrics.
5. Budget vs. Actual variance analysis.
6. Identification of margin drivers.
7. Productivity analysis.
8. Segmentation by business unit.
9. Construction of leading and lagging indicators.
10. Executive dashboard design.

**Analytical Architecture:**
```text
Operational Data
       ↓
Data Preparation
       ↓
KPI Model
       ↓
Business Rules
       ↓
Power BI / Python
       ↓
Executive Dashboard
       ↓
Decision Making
