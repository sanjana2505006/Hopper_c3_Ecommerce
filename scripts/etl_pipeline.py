"""
ETL Pipeline — Hopper C3 E-Commerce Capstone
Extracts raw data from Kaggle, cleans it, and exports to data/processed/.
Run: python scripts/etl_pipeline.py
"""

import pandas as pd
import numpy as np
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

RAW_DIR       = "data/raw"
PROCESSED_DIR = "data/processed"
OUTPUT_FILE   = os.path.join(PROCESSED_DIR, "cleaned_data.csv")


def extract(kaggle_dataset: str = "carrie1/ecommerce-data", filename: str = "data.csv") -> pd.DataFrame:
    log.info("Extracting dataset from Kaggle: %s", kaggle_dataset)
    try:
        import kagglehub
        path = kagglehub.dataset_download(kaggle_dataset)
        raw_path = os.path.join(path, filename)
    except Exception:
        raw_path = os.path.join(RAW_DIR, filename)
        log.info("kagglehub unavailable — loading from %s", raw_path)

    df = pd.read_csv(raw_path, encoding="latin1")
    log.info("Extracted: %s rows × %s cols", *df.shape)
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    initial = len(df)
    log.info("Step 1: Drop null CustomerID (%s nulls)", df["CustomerID"].isna().sum())
    df = df.dropna(subset=["CustomerID"])

    log.info("Step 2: Remove cancellations (InvoiceNo starts with C)")
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

    log.info("Step 3: Remove Quantity <= 0 and UnitPrice <= 0")
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    log.info("Step 4: Fill null Description")
    df["Description"] = df["Description"].fillna("Unknown")

    log.info("Step 5: Parse InvoiceDate, extract features")
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Month"]       = df["InvoiceDate"].dt.month
    df["Year"]        = df["InvoiceDate"].dt.year
    df["Day"]         = df["InvoiceDate"].dt.day_name()
    df["Hour"]        = df["InvoiceDate"].dt.hour
    df["Quarter"]     = df["InvoiceDate"].dt.quarter

    log.info("Step 6: Compute Revenue")
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    log.info("Step 7: Cast CustomerID to int")
    df["CustomerID"] = df["CustomerID"].astype(int)

    log.info("Step 8: Drop duplicates")
    before_dedup = len(df)
    df = df.drop_duplicates()
    log.info("  Dropped %s duplicates", before_dedup - len(df))

    log.info("Cleaning complete: %s → %s rows (removed %s)", initial, len(df), initial - len(df))
    return df.reset_index(drop=True)


def load(df: pd.DataFrame, path: str = OUTPUT_FILE) -> None:
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    df.to_csv(path, index=False)
    log.info("Saved cleaned data → %s (%s rows)", path, len(df))


def run():
    df_raw   = extract()
    df_clean = clean(df_raw)
    load(df_clean)
    log.info("ETL pipeline complete.")
    return df_clean


if __name__ == "__main__":
    run()
