import pandas as pd

txn = pd.read_csv("data/raw/08_investor_transactions.csv")
perf = pd.read_csv("data/raw/07_scheme_performance.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print("TRANSACTIONS")
print(txn.columns.tolist())

print("\nPERFORMANCE")
print(perf.columns.tolist())

print("\nAUM")
print(aum.columns.tolist())