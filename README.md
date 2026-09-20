# ⚙️ Industrial IoT Predictive Maintenance Analytics Platform

An end-to-end industrial data engineering and analytics dashboard engineered to track equipment health, monitor mechanical degradation, and diagnose failure modes across 10,000 milling machines.


## 📌 Executive Summary

Unplanned industrial downtime costs manufacturing facilities thousands of dollars per hour. This project implements a full-cycle operational intelligence pipeline using the **AI4I 2020 Predictive Maintenance Dataset**. 

Rather than relying purely on machine learning black boxes, this architecture focuses on **transparent physics-based feature formulation**, **relational staging and analytical aggregation in PostgreSQL**, and an **executive operations dashboard in Power BI** to enable immediate preventative maintenance interventions.


## 🛠️ Architecture & Tech Stack


Raw Sensor Stream (CSV)
          │
          ▼
 [ Python / Pandas ]   ──► Physics-based Feature Engineering (Power, ΔT, Overstrain)
          │
          ▼
  [ PostgreSQL DB ]    ──► Relational Schema, Wear Tier Binning & Analytical Views
          │
          ▼
 [ Power BI Desktop ]  ──► Operational Cockpit, Dynamic DAX KPIs, Interactive Slicers
