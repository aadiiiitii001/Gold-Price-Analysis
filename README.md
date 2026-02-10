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
