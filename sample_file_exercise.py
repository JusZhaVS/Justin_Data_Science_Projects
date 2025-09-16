import pandas as pd

#loading of file
df = pd.read_csv("retail_transactions.csv")

#convert to proper types
df["transaction_id"] = pd.to_numeric(df["transaction_id"], errors="coerce")
df["customer_id"] = pd.to_numeric(df["customer_id"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

#drop the invalid rows using this filter
mask_valid = (
    df["transaction_id"].notna()
    & df["customer_id"].notna()
    & df["date"].notna()
    & df["quantity"].notna()
    & df["price"].notna()
    & (df["quantity"] > 0)
    & (df["price"] > 0)
)
df = df[mask_valid].copy()

# compute revenue and add it as a new column
df["revenue"] = df["quantity"] * df["price"]

# Revenue per product
print("\nRevenue per product:")
print(df.groupby("product")["revenue"].sum().reset_index())

# Top 2 customers by spending
print("\nTop 2 customers by spending:")
print(
    df.groupby("customer_id")["revenue"]
    .sum()
    .reset_index()
    .sort_values("revenue", ascending=False)
    .head(2)
)
