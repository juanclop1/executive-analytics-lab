# 4. AI for Business Planning

## 📋 Business Context
Application of predictive analytics and planning scenarios to improve the ability to anticipate demand, production requirements, and capacity utilization in industrial operations.

The case is inspired by experiences in capacity and demand planning in highly critical industrial operations.

## 📊 Data Used
Synthetic dataset representing:
* Historical monthly demand.
* Different product families.
* Installed capacity.
* Available capacity.
* Historical production.
* Backlog.
* Lead times.
* Seasonal variables.
* Extraordinary events.
* Capacity constraints.

Between 36 and 60 months of historical data can be generated.

## 🔧 Methodology
1. Integration and cleaning of historical series.
2. Exploratory demand analysis.
3. Identification of trend and seasonality.
4. Anomaly detection.
5. Forecasting using statistical models.
6. Model comparison.
7. Scenario forecasting.
8. Translation of forecast into capacity requirements.
9. What-If simulation.
10. Visualization of results for Business Planning.

**Models:**
```text
Baseline
   ↓
Moving Average
   ↓
ARIMA / SARIMA
   ↓
Prophet
   ↓
Model Comparison
   ↓
Best Forecast
   ↓
Capacity Planning
   ↓
What-If Scenarios
