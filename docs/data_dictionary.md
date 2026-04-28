# Data Dictionary — UK Online Retail E-Commerce Dataset

## Dataset Summary

| Field | Value |
|---|---|
| Dataset Name | UK Online Retail |
| Source | Kaggle — carrie1/ecommerce-data |
| Raw File | data.csv |
| Original Source | UCI Machine Learning Repository |
| Last Updated | 2015 (static dataset) |
| Granularity | One row = one line item on one invoice |
| Raw Shape | 541,909 rows × 8 columns |
| Cleaned Shape | ~392,692 rows × 13 columns |
| Time Period | 2010-12-01 to 2011-12-09 |

---

## Raw Columns

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| InvoiceNo | string | Unique invoice number. 'C' prefix = cancellation | 536365 | EDA / KPI / Tableau | Cancellations (C-prefix) dropped |
| StockCode | string | Product/item code | 85123A | EDA / Tableau | No cleaning needed |
| Description | string | Product name | WHITE HANGING HEART T-LIGHT HOLDER | EDA / Tableau | 1,454 nulls filled with 'Unknown' |
| Quantity | integer | Units per line item (can be negative for returns) | 6 | KPI / EDA | Rows with Quantity ≤ 0 dropped |
| InvoiceDate | datetime | Date and time of invoice | 12/1/2010 8:26 | KPI / EDA / Tableau | Parsed to datetime; features extracted |
| UnitPrice | float | Price per unit in GBP (£) | 2.55 | KPI / EDA | Rows with UnitPrice ≤ 0 dropped |
| CustomerID | float (→ int) | Unique customer identifier | 17850 | KPI / EDA / Tableau | 135,080 nulls dropped; cast to int |
| Country | string | Country of the customer | United Kingdom | EDA / Tableau | 37 unique values; no cleaning needed |

---

## Derived Columns

| Derived Column | Logic | Business Meaning |
|---|---|---|
| Revenue | Quantity × UnitPrice | Total value of line item in GBP |
| Month | InvoiceDate.dt.month | Calendar month (1–12) for seasonal analysis |
| Year | InvoiceDate.dt.year | Year (2010 or 2011) |
| Day | InvoiceDate.dt.day_name() | Day of week name (e.g., 'Wednesday') |
| Hour | InvoiceDate.dt.hour | Hour of day for time-of-day analysis |
| Quarter | InvoiceDate.dt.quarter | Business quarter (1–4) |
| YearMonth | InvoiceDate period('M') | YYYY-MM string for monthly aggregation |
| R_Score | Recency quartile (1–5, 5=best) | RFM Recency score |
| F_Score | Frequency quartile (1–5, 5=best) | RFM Frequency score |
| M_Score | Monetary quartile (1–5, 5=best) | RFM Monetary score |
| RFM_Total | R_Score + F_Score + M_Score | Overall customer value score |
| Segment | Rule-based on R/F/M scores | Customer segment label |

---

## Data Quality Notes

- **CustomerID nulls:** 135,080 rows (24.9%) had no CustomerID — these cannot be attributed to a customer and were dropped before any customer-level analysis.
- **Cancellations:** ~9,288 rows had InvoiceNo starting with 'C' (cancellation). These were removed as they represent reversed transactions.
- **Negative Quantity / UnitPrice:** Small number of rows had zero or negative values (data entry errors / returns); all removed.
- **Duplicate rows:** 5,192 exact duplicate rows dropped.
- **UK dominance:** 88.9% of cleaned rows are from United Kingdom. Country-level analysis splits UK vs. Non-UK.
- **Partial month:** December 2011 has only 9 days of data (cut-off date: 2011-12-09). Excluded from monthly growth and forecasting calculations.
- **Outliers in Quantity/UnitPrice:** Right-skewed distributions. Max Quantity = 80,995 (PAPER CRAFT, LITTLE BIRDIE — single bulk order). Revenue plots clipped at 500 for visualization clarity.

---

## KPI Framework

| KPI | Definition | Formula |
|---|---|---|
| Total Revenue | Sum of all transaction revenue | SUM(Revenue) |
| Average Order Value (AOV) | Mean invoice total | SUM(Revenue) / COUNT(DISTINCT InvoiceNo) |
| Repeat Purchase Rate | % customers with more than 1 invoice | COUNT(customers with orders > 1) / COUNT(all customers) × 100 |
| Monthly Revenue Growth (MoM) | % change in revenue month-over-month | (Rev_M − Rev_M−1) / Rev_M−1 × 100 |
| Revenue per Customer | Mean total spend per customer | SUM(Revenue) / COUNT(DISTINCT CustomerID) |
| UK Revenue Share | % of total revenue from United Kingdom | UK Revenue / Total Revenue × 100 |
| RFM Segmentation | Customer value classification | Rule-based scoring on Recency, Frequency, Monetary dimensions |
