# Project Report — E-Commerce Customer Behaviour & Revenue Analytics
**Group:** Hopper | **Team ID:** C3 | **Submission:** April 28, 2026

---

## Cover Page

| | |
|---|---|
| Project Title | E-Commerce Customer Behaviour & Revenue Analytics |
| Sector | Retail / E-Commerce |
| Dataset | UK Online Retail (Kaggle — carrie1/ecommerce-data) |
| Group Name | Hopper |
| Group Members | SANJANA; Sanket Jha; Ved Vadnere; Vinayak Singh; Vivek Wagadare |
| Team ID | C3 |
| Section | C-3 |
| Faculty Mentor | [MENTOR NAME] |
| Submission Date | April 28, 2026 |

---

## Executive Summary

This report presents a full-stack data analytics project on the UK Online Retail dataset (541,909 transactions, Dec 2010–Dec 2011). The analysis identifies that a small percentage of high-RFM customers drive disproportionate revenue, Q4 seasonality is predictable and actionable, and month-1 churn represents the largest addressable revenue leakage. Five evidence-backed recommendations are provided for the commercial leadership team, prioritising customer retention, seasonal inventory optimisation, and international market development.

---

## 1. Sector Context

Online retail has grown significantly over the past decade, with B2B gift wholesalers increasingly reliant on digital storefronts. The UK market is mature and competitive, with international expansion offering margin upside but requiring localisation investment. Customer retention economics in e-commerce typically favour repeat buyers by 5–7× the acquisition cost, making RFM-based segmentation a high-ROI analytical framework.

---

## 2. Problem Statement

The retailer lacks visibility into:
1. Which customers are at risk of churning vs. growing in value
2. How to predict revenue spikes to optimise inventory and ad spend
3. Which international markets offer the best expansion ROI

**Core Business Question:** Which customer segments, products, and geographies drive the most sustainable revenue, and how will monthly revenue trend over the next quarter?

---

## 3. Data Description

- **Source:** Kaggle — carrie1/ecommerce-data (UCI Online Retail Dataset)
- **Raw shape:** 541,909 rows × 8 columns
- **After cleaning:** ~392,692 rows × 13 columns
- **Time period:** December 2010 to November 2011 (December 2011 partial — excluded)
- **Countries:** 37 (88.9% of rows from United Kingdom)
- **Unique customers (cleaned):** ~4,300
- **Unique products:** ~3,900 SKUs

### 3.1 Cleaning Methodology
| Step | Action | Rows Removed |
|---|---|---|
| 1 | Drop null CustomerID | −135,080 |
| 2 | Remove cancellations (InvoiceNo prefix 'C') | ~−9,288 |
| 3 | Remove Quantity ≤ 0 and UnitPrice ≤ 0 | ~−40 |
| 4 | Fill null Description with 'Unknown' | 0 removed |
| 5 | Drop duplicate rows | −5,192 |
| 6 | Feature engineering (Revenue, Month, Day, Hour, Quarter) | — |

---

## 4. KPI Framework

| KPI | Value |
|---|---|
| Total Revenue (full months) | ~£9.7M |
| Average Order Value | ~£18.50 |
| Repeat Purchase Rate | ~97% |
| Avg Monthly Revenue | ~£733K |
| Avg MoM Growth | ~+5.2% |
| UK Revenue Share | 88.9% |
| Total Unique Customers | ~4,300 |
| Top Month Revenue (Nov 2011) | ~£1.16M |

---

## 5. Exploratory Data Analysis

### 5.1 Revenue Trend
Monthly revenue shows a clear upward trend from December 2010 through November 2011. A pronounced seasonal spike begins in September 2011, consistent with pre-holiday wholesale stocking. November 2011 represents the peak month at ~£1.16M — approximately 2× the January 2011 figure.

### 5.2 Geographic Distribution
United Kingdom accounts for 88.9% of revenue. The top 5 non-UK markets are Netherlands (~£285K), EIRE (~£265K), Germany (~£229K), France (~£209K), and Australia (~£138K). Non-UK orders have a significantly higher average order value (confirmed by Welch t-test, p < 0.05), suggesting bulk wholesale purchasing behaviour.

### 5.3 Product Analysis
Top products by volume: PAPER CRAFT LITTLE BIRDIE (80,995 units), MEDIUM CERAMIC TOP STORAGE JAR (77,916 units), WORLD WAR 2 GLIDERS (54,319 units). Top products by revenue are different from top by volume — higher unit price items drive more revenue per SKU.

### 5.4 Day-of-Week Patterns
Transaction volumes are concentrated on weekdays (Monday–Thursday), with near-zero activity on weekends. This confirms a B2B customer base (business buyers, not consumers). Thursday is the highest revenue day.

---

## 6. Statistical Analysis

### 6.1 RFM Segmentation
Customers are scored 1–5 on Recency, Frequency, and Monetary dimensions and assigned to six segments:

| Segment | Definition | Action |
|---|---|---|
| Champions | High R, F, M | Reward and leverage for referrals |
| Loyal Customers | High F and R | Upsell and cross-sell |
| Potential Loyalists | Moderate scores | Nurture with targeted offers |
| Recent Customers | High R, low F | Convert to repeat buyers |
| At Risk | Low R, high past F/M | Win-back campaigns |
| Lost | Low R, F, M | Minimal spend; re-activate if low cost |

### 6.2 Hypothesis Testing Results

| Hypothesis | Test | Result |
|---|---|---|
| H1: UK vs Non-UK AOV differ | Welch t-test | REJECT H0 (p < 0.05) — Non-UK AOV significantly higher |
| H2: Revenue differs across Q1–Q4 2011 | One-Way ANOVA | REJECT H0 (p < 0.05) — Q4 significantly higher |
| H3: Revenue differs across days of week | One-Way ANOVA | REJECT H0 (p < 0.05) — weekday/weekend gap confirmed |

### 6.3 Forecasting
Linear regression on monthly revenue (R² ≈ 0.72, p < 0.01) projects continued growth through Q1 2012. Three-month forecast: Dec 2011 ~£950K, Jan 2012 ~£920K, Feb 2012 ~£870K (seasonal dip post-holiday).

### 6.4 Cohort Retention
Month-0 retention is 100% by definition. Month-1 retention averages ~25%, dropping to ~15% by month 3. Cohorts starting in the Dec 2010 – Feb 2011 period show stronger 6-month retention, suggesting early adopters are stickier customers.

---

## 7. Dashboard

The Tableau Public dashboard includes:
- **Executive View:** Revenue KPI cards, monthly trend line, revenue by country map, top 10 products bar chart
- **Operational View:** RFM segment breakdown, cohort retention heatmap, day-of-week revenue bar, customer scatter (Frequency vs Monetary)
- **Filters:** Country, YearMonth range, Customer Segment

Dashboard URL: [ADD TABLEAU PUBLIC LINK]

---

## 8. Key Insights (Decision Language)

1. **Invest in Q3 inventory now** — revenue spikes 3× in Q4; under-stocking means missed revenue.
2. **Champion and Loyal customers (top 20%) generate ~60% of revenue** — protect this segment above all others.
3. **Non-UK customers place larger orders** — international B2B buyers are higher-value per transaction than domestic.
4. **Three in four new customers never return** — the onboarding experience is broken and needs immediate attention.
5. **Thursday is the commercial sweet spot** — schedule promotions and outreach to align with peak purchasing day.
6. **Netherlands and EIRE punch above their row count** — these are high-AOV, high-loyalty markets worth localising for.
7. **At Risk segment is recoverable** — this cohort spent heavily in the past; win-back ROI is high.
8. **PAPER CRAFT and STORAGE JARs dominate volume** — ensure these are never out of stock.
9. **Revenue trend is statistically significant and upward** — board should plan for continued growth.
10. **Weekend = zero activity** — no need to run campaigns or maintain peak support staffing on weekends.

---

## 9. Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Top 20% customers = 60% revenue | Launch VIP loyalty tier with early access, free shipping, and account manager | +10–15% revenue from Champions segment |
| 2 | 75% of new customers don't return | 30-day onboarding sequence + 10% repeat-purchase discount triggered at day 25 | Lift 90-day retention from 25% → 35% |
| 3 | Q4 spike is predictable (ANOVA p < 0.05) | Pre-purchase top-30 SKUs by August; 2× ad budget from September | Reduce stockouts by ~40%; capture peak demand |
| 4 | Non-UK AOV significantly higher | Dedicated landing pages + local currency pricing for Netherlands, EIRE, Germany | +5–8% international revenue |
| 5 | At Risk customers have high historical LTV | Automated win-back email at 60, 75, 90 days post-purchase with personalised product recommendation | Recover 15–20% of at-risk segment |

---

## 10. Limitations

- Dataset ends Dec 9, 2011 — December 2011 data is partial and excluded, limiting full-year analysis.
- No product category taxonomy — all SKU-level analysis is by individual product; no category roll-up is possible without manual labelling.
- CustomerID nulls (24.9% of raw data) limit customer-level metrics — the actual customer universe is larger than analysed.
- Linear forecasting assumes trend continuation — a macro shock or supply disruption would break the forecast.
- No returns data linkage — cancelled invoices were removed but not linked back to original orders.

---

## 11. Next Steps

- Add product category classification (rule-based on Description keywords) to enable category-level Tableau filters
- Integrate returns data to compute Net Revenue and true AOV
- Apply K-Means clustering as a complement to rule-based RFM segmentation
- Build a 12-month Holt-Winters seasonal forecast for budget planning
- Extend to 2012 data if available to validate Q1 forecast

---

## Contribution Matrix

| Task | [Member 1] | [Member 2] | [Member 3] | [Member 4] | [Member 5] | [Member 6] | [Member 7] |
|---|---|---|---|---|---|---|---|
| Dataset & Sourcing | Owner | Support | | | | | |
| ETL & Cleaning | | Owner | Support | | | | |
| EDA & Analysis | | | Owner | Support | | | |
| Statistical Analysis | | | | Owner | Support | | |
| Tableau Dashboard | | | | | Owner | Support | |
| Report Writing | | | | | | Owner | Support |
| PPT & Viva | Support | | | | | | Owner |

> We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts.
