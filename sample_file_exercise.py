import sys
from typing import Dict,Tuple

import pandas as pd
import numpy as np

def load_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)

    df["transaction_id"] = pd.to_numeric(df["transaction_id"], errors="coerce")
    df["customer_id"] = pd.to_numeric(df["customer_id"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"], errors="coerce", utc=False)

    if "product" in df.columns:
        df["product"] = (
            df["product"]
            .astype("string")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.title()
        )

    return df

def data_quality_report(df: pd.DataFrame) -> Dict:
    issues = {
        "missing values": df.isna().sum().to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "invalid_quantity": int( ( (df["quantity"] <= 0) | df["quantity"].isna() ).sum()),
        "invalid_price": int( (df["price"] <= 0 | df["price"].isna()).sum()  ),
        "invalid_ids": int(
            (df["transaction_id"].isna() | df["customer_id"].isna()).sum()    
        ),
        "invalid_dates": int(df["date"].isna().sum()),
        "unique_products": sorted(df["product"].dropna().unique().tolist()),
        "row_count": int(len(df)),
    }
    return issues

