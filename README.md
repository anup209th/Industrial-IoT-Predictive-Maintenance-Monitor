# Industrial IoT Predictive Maintenance Monitor

An end-to-end data analytics engineering project designed to monitor milling machine operations, assess equipment degradation, and identify root causes of mechanical failure. Built using Python (Feature Engineering & Physics Calculations), PostgreSQL (Analytical Storage & Transformation), and Power BI (Interactive Monitoring Dashboard).

---

## 📌 Project Overview
Industrial machinery generates high-frequency operational telemetry. Without proactive monitoring, undetected component wear and heat dissipation bottlenecks cause unplanned downtime. This project ingests raw telemetry from the AI4I 2020 Predictive Maintenance Dataset (10,000 industrial records), enriches the signals with derived mechanical engineering equations, processes analytical aggregations in PostgreSQL, and presents an interactive executive operations cockpit in Power BI.

---

## 🛠️ Tech Stack & Architecture

Raw Sensor Data (CSV)
         │
         ▼
[Python / Pandas] ──► Physics Feature Engineering (Power, Delta T, Overstrain)
         │
         ▼
[PostgreSQL DB]   ──► Relational Schema, Risk Binning & Aggregations
         │
         ▼
[Power BI Desktop] ──► KPI Cards, Stress Profiles, Operating Envelope, Watchlist

- Python 3.x (pandas, numpy): Raw sensor ETL, mathematical calculations of mechanical energy, and consolidated failure categorization.
- PostgreSQL (pgAdmin 4): Relational database structuring, aggregated wear-tier profiling, and data staging.
- Power BI Desktop: Custom DAX measures, cross-filtering operational parameters, and interactive dashboard visuals.

---

## ⚙️ Engineering Calculations & Feature Formulation

To extract deeper insights beyond raw temperature and RPM, three physical engineering features were engineered via Python:

1. Mechanical Power (P in kW): Derived from angular speed and torque:
   Power (kW) = (2 * pi * Rotational Speed [RPM] * Torque [Nm]) / (60 * 1000)

2. Temperature Difference (Delta T in K): Measures cooling efficiency bottleneck:
   Delta Temp (K) = Process Temperature - Air Temperature

3. Overstrain Index: Tracks cumulative physical stress on the cutting tool:
   Overstrain Index = Tool Wear [min] * Torque [Nm]

---

## 🗄️ Database Architecture & SQL Transformations

Data was loaded into predictive_maintenance_db and modeled into three specific analytics tables:

- equipment_telemetry: The base telemetry table with all 10,000 records, physical features, and single-class failure classifications.
- agg_failure_modes: Failure breakdown aggregated across machine quality variants (L, M, H):
  * Low Variant (L): 6,000 machines | 235 failures (3.92% failure rate)
  * Medium Variant (M): 2,997 machines | 83 failures (2.77% failure rate)
  * High Variant (H): 1,003 machines | 21 failures (2.09% failure rate)
- agg_tool_stress_profile: Binned wear tiers (0-60m, 60-120m, 121-180m, >180m) showing that failure rates spike over 4x once tool wear exceeds 180 minutes (~9.2%).

---

## 📊 Dashboard Visuals & Core DAX Measures

### Core DAX Measures:
- Total Machines = COUNTROWS('equipment_telemetry_bi')
- Total Failures = SUM('equipment_telemetry_bi'[machine_failure])
- Failure Rate % = DIVIDE([Total Failures], [Total Machines], 0)
- Avg Power (kW) = AVERAGE('equipment_telemetry_bi'[power_kw])

### Key Visuals:
1. Executive KPI Summary Cards: Total Machines (10K), Total Failures (339), Overall Failure Rate (3.39%), Avg Power (6.28 kW).
2. Root Cause Breakdown (Horizontal Bar Chart): Isolates primary drivers—Heat Dissipation (115) and Power/Overstrain Failures dominate.
3. Tool Wear Risk Profile (Column Chart): Displays exponential risk increase across wear tiers.
4. Operating Envelope (Scatter Plot): Plots Torque vs. RPM, highlighting failure clusters at extreme boundaries (high-torque stalls and high-speed burnouts).
5. Failures by Product Variant (Donut Chart): Visualizes failure distribution skewed toward low-cost variants (L).
6. Critical Equipment Watchlist (Interactive Table): Actionable per-machine telemetry log for plant engineers.

---

## 🚀 How to Run

1. Clone the Repository:
   git clone https://github.com/<your-username>/industrial-iot-predictive-maintenance.git
   cd industrial-iot-predictive-maintenance

2. Execute Python Pipeline:
   pip install pandas numpy
   python data_pipeline.py

3. Load SQL Schemas:
   Open pgAdmin 4, execute the DDL queries to create the staging tables and analytical views.

4. Open Dashboard:
   Launch predictive_maintenance_dashboard.pbix in Power BI Desktop.
