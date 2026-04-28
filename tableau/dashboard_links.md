# Tableau Dashboard Links

## Published Dashboard

| View | URL |
|---|---|
| Tableau Public Dashboard | https://public.tableau.com/views/Hopper_C3_Ecommerce_Dashboard/Dashboard1 |
| Executive View | https://public.tableau.com/views/Hopper_C3_Ecommerce_Dashboard/Dashboard1 |
| Operational View | https://public.tableau.com/views/Hopper_C3_Ecommerce_Dashboard/Dashboard1 |

## Dashboard Filters
- Country (UK / Non-UK / All)
- Year-Month range
- Customer Segment (RFM)
- Product Category

## Screenshots
See `tableau/screenshots/` for:
- `rfm_segmentation.png` — RFM customer segment breakdown
- `time_series_forecast.png` — Monthly revenue trend + 3-month forecast
- `cohort_retention.png` — Customer cohort retention heatmap

## Data Sources Used in Dashboard
- `data/processed/cleaned_data.csv` — main transaction data
- `data/processed/kpi_monthly.csv` — monthly KPI trends
- `data/processed/kpi_country.csv` — revenue by country
- `data/processed/kpi_top_products.csv` — top 100 products
- `data/processed/kpi_customers.csv` — customer-level summary
- `data/processed/rfm_segments.csv` — RFM segment labels
