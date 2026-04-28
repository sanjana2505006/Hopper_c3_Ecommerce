# Presentation Outline — 12 Slides
## E-Commerce Customer Behaviour & Revenue Analytics | Hopper C3

---

**Slide 1 — Title**
- Project Title: E-Commerce Customer Behaviour & Revenue Analytics
- Sector: Retail / E-Commerce
- Team ID: C3 | Group: Hopper
- Members: [NAME1]; [NAME2]; [NAME3]; [NAME4]; [NAME5]; [NAME6]; [NAME7]
- Faculty Mentor: [NAME] | Date: April 28, 2026

---

**Slide 2 — Context & Problem Statement**
- Sector: UK B2B online wholesale retail
- Stakeholder: Commercial Director / Revenue Operations
- Core Question: Which customers, products, and geographies drive sustainable revenue?
- Objective: Segment customers by value; forecast revenue; deliver 5 actionable recommendations

---

**Slide 3 — Data Engineering**
- Source: UK Online Retail Dataset (Kaggle / UCI), 541,909 raw rows
- Cleaning: Dropped 135K null CustomerIDs, cancelled invoices, zero-price rows, 5K duplicates
- Final: 392,692 rows × 13 columns | Dec 2010 – Nov 2011
- Data dictionary: 8 raw columns + 5 derived features (Revenue, Month, Day, Hour, Quarter)

---

**Slide 4 — KPI Framework**
- Total Revenue: ~£9.7M | AOV: ~£18.50
- Repeat Purchase Rate: ~97% | Unique Customers: ~4,300
- Avg Monthly Revenue: ~£733K | Avg MoM Growth: ~+5.2%
- UK Revenue Share: 88.9%

---

**Slide 5 — Key EDA Insights**
1. Revenue spikes 3× in Q4 (Sep–Nov 2011) — predictable seasonal pattern
2. UK = 88.9% revenue but non-UK orders have higher AOV
3. Top 3 products by volume: PAPER CRAFT, STORAGE JAR, GLIDERS
4. Near-zero weekend transactions — confirmed B2B customer base
5. Thursday is peak revenue day; Monday second highest

---

**Slide 6 — Advanced Analysis**
- RFM Segmentation: 6 segments (Champions / Loyal / Potential / Recent / At Risk / Lost)
- Hypothesis Testing: H1 (UK vs Non-UK AOV, t-test, p<0.05), H2 (Quarterly ANOVA, p<0.05), H3 (Day-of-week ANOVA, p<0.05)
- Time Series: Linear trend R²≈0.72, upward slope ~£50K/month
- Cohort Analysis: Month-1 retention ~25%; long-tenure cohorts show stronger stickiness

---

**Slide 7 — Dashboard Overview**
- Executive View: KPI cards, monthly trend, revenue map, top products
- Operational View: RFM breakdown, cohort heatmap, day-of-week bar, customer scatter
- Filters: Country · Date Range · Customer Segment
- [INSERT DASHBOARD SCREENSHOT]
- Link: [ADD TABLEAU PUBLIC URL]

---

**Slide 8 — Top Insights**
1. Champions (top RFM) = ~60% of revenue from ~15% of customers
2. At Risk customers have high historical LTV — recoverable with win-back
3. Non-UK bulk orders drive higher AOV — international expansion is margin-positive
4. Q4 seasonality is statistically confirmed — inventory and ad spend should front-load Q3

---

**Slide 9 — Recommendations**
| # | Recommendation | Expected Impact |
|---|---|---|
| 1 | VIP loyalty programme for Champions | +10–15% top-segment revenue |
| 2 | 30-day onboarding + repeat-purchase discount | Retention 25% → 35% |
| 3 | Pre-stock top-30 SKUs by August | -40% stockouts in Q4 |
| 4 | Localise for Netherlands, EIRE, Germany | +5–8% international revenue |
| 5 | Win-back emails at 60/75/90 days | Recover 15–20% At Risk segment |

---

**Slide 10 — Impact Assessment**
- Priority 1 (High impact, Low effort): Win-back email campaign — immediate revenue recovery
- Priority 2 (High impact, Medium effort): Onboarding sequence — long-term retention improvement
- Priority 3 (High impact, High effort): VIP loyalty tier — structural revenue uplift
- Feasibility: All recommendations use existing customer data with no new data collection required

---

**Slide 11 — Limitations**
- Dec 2011 partial data excluded — limits full-year view
- No product category taxonomy — SKU-level only
- 24.9% of raw records had no CustomerID — customer universe is larger than analysed
- Linear forecast assumes trend continuation — macro shocks not modelled

---

**Slide 12 — Next Steps & Close**
- Add product category labelling for category-level Tableau drill-downs
- Apply K-Means clustering as complement to rule-based RFM
- Extend to 2012 data (if available) to validate forecast
- Build Holt-Winters seasonal model for budget planning
- Thank you | Questions welcome
