# 📊 Gold Price Analytics & Business Intelligence Project

## Overview
This project demonstrates an end-to-end data analytics workflow using historical gold price data.  
It focuses on data quality, reproducibility, statistical analysis, SQL-based insights, and business-ready visualization.

The objective is to extract actionable insights that support data-driven decision-making, not just generate charts.

---

## Business Problem
Gold prices are volatile and influenced by market and macroeconomic factors.  
Organizations require:
- trend identification
- volatility analysis
- period-over-period comparison
- reliable, validated datasets for reporting

This project answers:
- How has gold price evolved over time?
- Which periods exhibit the highest volatility?
- What are the long-term vs short-term trends?
- How can these insights be delivered to business stakeholders?

---

## Dataset
- Source: Historical gold price dataset (CSV)
- Granularity: Daily prices
- Type: Time-series data

Raw data is preserved and never modified directly.

---

## Project Structure
```text
gold-price-analysis/
│
├── data/
│ ├── raw/
│ │ └── gold_historical_data.csv
│ └── processed/
│ └── gold_cleaned.csv
│
├── notebooks/
│ ├── 01_data_quality_checks.ipynb
│ ├── 02_eda.ipynb
│ ├── 03_feature_engineering.ipynb
│ └── 04_statistical_analysis.ipynb
│
├── scripts/
│ └── data_cleaning.py
│
├── sql/
│ └── analysis_queries.sql
│
├── powerbi/
│ └── gold_dashboard.pbix
│
└── README.md
```
---

## Workflow

### 1. Data Quality & Validation
- Schema inspection
- Missing value detection
- Duplicate identification
- Date validation and consistency checks

Notebook:
- `01_data_quality_checks.ipynb`

---

### 2. Automated Data Cleaning
Cleaning is automated to ensure reproducibility:
- Column standardization
- Date parsing and sorting
- Removal of invalid and duplicate records
- Validation using assertions
- Output saved to the `processed/` directory

Run:
```bash
python scripts/data_cleaning.py
```

---
### 3. Exploratory Data Analysis (EDA)

- Price trends over time

- Yearly and monthly aggregation

- Volatility identification

- Distribution analysis

Notebook:

02_eda.ipynb
---

### 4. Feature Engineering

- Derived features include:

- Daily returns

- Rolling averages

- Rolling volatility metrics

- These features support KPI creation and downstream analysis.

Notebook:
```bash
03_feature_engineering.ipynb
```
5. Statistical Analysis

- Descriptive statistics

- Volatility comparison across time periods

- Trend interpretation

Notebook:
```
04_statistical_analysis.ipynb
```
6. SQL-Based Analysis

- SQL-style analytical queries are used to:

- Aggregate prices by year

- Measure volatility

- Compare long-term trends

File:
```
sql/analysis_queries.sql
```
7. Power BI Dashboard

An interactive Power BI dashboard is built on cleaned data:

- Time-series gold price trends

- KPI cards (average price, volatility, highs/lows)

- Year and month slicers

- Business-focused data storytelling

File:
```
powerbi/gold_dashboard.pbix
```

Tools & Technologies

- Python (Pandas, NumPy, Matplotlib)

- SQL

- Power BI

- Jupyter Notebook

Git

Key Skills Demonstrated

- Data cleaning and validation

- Exploratory data analysis (EDA)

- Statistical reasoning

- SQL analytics

- Dashboard design and KPI development

- Automation and reproducibility

- Business-oriented data storytelling

Notes
```
Raw data is immutable
```
All transformations are documented and reproducible

Every metric in Power BI is traceable to Python logic
