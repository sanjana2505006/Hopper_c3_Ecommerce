# Hopper_c3_Ecommerce — NST DVA Capstone 2

## Project Overview

| Field | Details |
|---|---|
| Project Title | E-Commerce Customer Behaviour & Revenue Analytics |
| Sector | Retail / E-Commerce |
| Team ID | C3 |
| Group Name | Hopper |
| Section | C-3 |
| Faculty Mentor | Kajal Badlani |
| Institute | [INSTITUTE NAME] |
| Submission Date | April 28, 2026 |

---

## Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead | Sanjana | sanjana2505006 |
| Data Lead + Analysis Lead | Sanket Jha | learn-dumboo24 |
| ETL Lead | Ved Vadnere | [GITHUB] |
| Visualization Lead | Vivek Wagadare | [GITHUB] |
| Strategy Lead + PPT Lead | Vinayak Singh | [GITHUB] |

> **Group Members:** SANJANA; Sanket Jha; Ved Vadnere; Vinayak Singh; Vivek Wagadare

---

## Business Problem

The UK-based online retailer operates across 37 countries and generates millions of transactions annually. Despite strong overall revenue, the business lacks visibility into which customer segments drive long-term value, which markets are under-performing relative to potential, and how revenue seasonality can be predicted to optimise inventory and marketing spend. Without data-driven segmentation and forecasting, the business risks over-investing in low-value customers and missing peak demand signals.

**Core Business Question:**  
Which customer segments, products, and geographies drive the most sustainable revenue, and how will monthly revenue trend over the next quarter?

**Decision Supported:**  
This analysis enables the commercial team to prioritise retention investment toward Champion and Loyal customer segments, deprioritise international markets with low repeat rates, and adjust inventory procurement ahead of the Q4 seasonal spike.

---

## Dataset

| Field | Value |
|---|---|
| Source Name | UK Online Retail Dataset |
| Direct Access Link | https://www.kaggle.com/datasets/carrie1/ecommerce-data |
| Row Count (raw) | 541,909 |
| Row Count (cleaned) | ~392,692 |
| Column Count | 8 raw → 13 cleaned |
| Time Period Covered | December 2010 – December 2011 |
| Format | CSV (latin1 encoding) |

### Key Columns Used

| Column Name | Description | Role in Analysis |
|---|---|---|
| InvoiceNo | Unique transaction ID | Order counting, grouping |
| CustomerID | Unique customer identifier | RFM, segmentation, retention |
| InvoiceDate | Date and time of purchase | Time series, seasonality |
| Quantity | Units purchased per line item | Volume KPIs |
| UnitPrice | Price per unit (£) | Revenue computation |
| Country | Customer country | Geographic analysis |
| Revenue | Quantity × UnitPrice (derived) | Primary KPI metric |
| Segment | RFM-based customer label (derived) | Segmentation analysis |

---

## KPI Framework

| KPI | Definition | Formula / Computation |
|---|---|---|
| Total Revenue | Sum of all transaction revenue | SUM(Revenue) |
| Average Order Value (AOV) | Mean invoice total | SUM(Revenue) / COUNT(DISTINCT InvoiceNo) |
| Repeat Purchase Rate | % customers with > 1 invoice | Notebook 05 → kpi_customers.csv |
| Monthly Revenue Growth (MoM %) | % change month-over-month | (Rev_M − Rev_M−1) / Rev_M−1 × 100 |
| Revenue per Customer | Mean total spend per customer | SUM(Revenue) / COUNT(DISTINCT CustomerID) |
| UK Revenue Share (%) | % of total revenue from UK | UK_Rev / Total_Rev × 100 |
| RFM Score | Customer value score (3–15) | R + F + M quintile scores |
| Cohort Retention Rate | % of customers returning each month | Cohort pivot ÷ cohort size |

---

## Tableau Dashboard

| Field | Value |
|---|---|
| Dashboard URL | [ADD TABLEAU PUBLIC LINK] |
| Executive View | KPI summary — total revenue, AOV, top countries, monthly trend |
| Operational View | RFM segments, top products, cohort retention, day-of-week patterns |
| Main Filters | Country · Year-Month range · Customer Segment |

See `tableau/dashboard_links.md` and `tableau/screenshots/`.

---

## Key Insights

1. **Revenue is strongly seasonal** — Q4 2011 (Sep–Nov) generated 3× the monthly average of Q1, driven by holiday demand.
2. **UK accounts for 88.9% of revenue** but only ~66% of unique customers — UK customers have higher spend per order.
3. **Champion customers (top RFM segment)** represent ~15% of the customer base but contribute disproportionate revenue.
4. **At Risk customers** (high historical spend, low recency) represent a recoverable revenue opportunity through targeted re-engagement.
5. **Average Order Value (AOV)** for non-UK customers is significantly higher than UK (Welch t-test, p < 0.05) — international orders tend to be bulk purchases.
6. **Thursday and Wednesday are peak revenue days** — weekend transaction volumes are near zero (B2B retail pattern).
7. **Monthly revenue grew at a compound rate** with strong linear trend (R² > 0.7), supporting Q1 2012 forecast of continued growth.
8. **Top 10 products** account for ~18% of total units sold; PAPER CRAFT and STORAGE JARS dominate volume.
9. **Cohort retention drops sharply** after month 1 — only ~25% of new customers make a second purchase within 90 days.
10. **Netherlands, EIRE, and Germany** are the highest-revenue non-UK markets with consistent repeat purchasing.

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Champion customers drive outsized revenue | Launch VIP loyalty programme targeting top RFM quintile with exclusive early access and discounts | +10–15% revenue from top segment |
| 2 | At Risk customers (high past spend, low recency) | Deploy automated win-back email campaign 60–90 days after last purchase | Recover 15–20% of at-risk customers |
| 3 | Q4 seasonal spike is predictable | Pre-build inventory for top 20 products by August; increase digital ad spend from September | Reduce stockouts; capture peak demand |
| 4 | Month-1 churn is high (~75% of new customers don't return) | Implement onboarding email sequence + first-repeat-purchase discount within 30 days | Improve 90-day retention from 25% → 35% |
| 5 | International orders have higher AOV | Invest in localised storefronts for Netherlands, Germany, and France | +5–8% international revenue |

---

## Contribution Matrix

| Task | Sanjana | Sanket Jha |
|---|---|---|
| Dataset & Sourcing | Owner | |
| Data Loading & Initial EDA (NB 01–03) | Owner | |
| ETL Cleaning Pipeline (NB 02) | | Owner |
| Statistical Analysis (NB 04) | | Owner |
| KPI Computation & Final Load (NB 05) | | Owner |
| Tableau Dashboard | | Owner |
| Report Writing | | Owner |

> We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts. — Team Lead: Sanjana

---

## Repository Structure

```
Hopper_c3_Ecommerce/
├── README.md
├── data/
│   ├── raw/                          # Original dataset (Kaggle download)
│   └── processed/                    # Cleaned pipeline outputs
│       ├── cleaned_data.csv
│       ├── kpi_monthly.csv
│       ├── kpi_country.csv
│       ├── kpi_top_products.csv
│       ├── kpi_customers.csv
│       ├── kpi_day_of_week.csv
│       └── rfm_segments.csv
├── notebooks/
│   ├── 01_extraction.ipynb           # Data loading from Kaggle
│   ├── 02_cleaning.ipynb             # ETL cleaning pipeline
│   ├── 03_eda.ipynb                  # Exploratory data analysis
│   ├── 04_statistical_analysis.ipynb # RFM, hypothesis testing, forecasting
│   └── 05_final_load_prep.ipynb      # KPI computation + Tableau exports
├── scripts/
│   └── etl_pipeline.py               # Standalone ETL script
├── tableau/
│   ├── screenshots/                  # Dashboard PNG exports
│   └── dashboard_links.md            # Tableau Public URL
├── reports/
│   ├── project_report.md             # Full project report
│   └── presentation_outline.md       # 12-slide deck outline
├── docs/
│   └── data_dictionary.md            # Column definitions + KPI framework
├── DVA-oriented-Resume/
└── DVA-focused-Portfolio/
```

---

## Academic Integrity

All analysis, code, and recommendations in this repository are the original work of the team listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.
