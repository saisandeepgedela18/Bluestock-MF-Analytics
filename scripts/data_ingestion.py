import pandas as pd
import matplotlib.pyplot as plt

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

top_funds = fund_master.sort_values(
    by="min_lumpsum_amount",
    ascending=False
).head(10)

plt.figure(figsize=(10,6))

plt.barh(
    top_funds["scheme_name"],
    top_funds["min_lumpsum_amount"]
)

plt.title("Top 10 Funds by Minimum Lumpsum Amount")
plt.xlabel("Minimum Investment (₹)")
plt.ylabel("Scheme Name")

plt.tight_layout()
plt.show()