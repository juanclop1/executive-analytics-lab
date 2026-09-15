# 3. PMO & Project Controls Analytics

## 📋 Business Context
Project Controls model to consolidate a portfolio of projects, identify early deviations, and provide an executive view of cost, schedule, progress, and risk.

The case is inspired by experiences in controlling large infrastructure, energy, and Oil & Gas projects.

## 📊 Data Used
Synthetic dataset of a portfolio composed of:
* 20 projects.
* Budget per project.
* Planned Value (PV).
* Earned Value (EV).
* Actual Cost (AC).
* Physical progress.
* Planned and actual dates.
* Risks.
* Corrective actions.
* Owners.
* Project status.

The dataset allows reproducing portfolio analysis without using confidential contractual information.

## 🔧 Methodology
1. Portfolio structuring.
2. Baseline definition.
3. Consolidation of physical and financial progress.
4. Earned Value Management (EVM) calculation.
5. Variance identification.
6. CPI and SPI calculation.
7. Forecast analysis.
8. Risk integration.
9. Classification of projects by exposure level.
10. Executive dashboard construction.

**EVM Model:**
```text
PV → Planned Value
EV → Earned Value
AC → Actual Cost

CPI = EV / AC
SPI = EV / PV
