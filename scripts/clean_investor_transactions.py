import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Valid amount
df = df[df["amount_inr"] > 0]

# KYC validation
valid_kyc = ["Yes", "No", "Pending"]

df = df[
    df["kyc_status"].isin(valid_kyc)
]

# Remove duplicates
df = df.drop_duplicates()

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions Cleaned")
print(df.shape)