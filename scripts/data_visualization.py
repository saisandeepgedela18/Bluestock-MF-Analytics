import pandas as pd
import matplotlib.pyplot as plt

fund_master = pd.read_csv("data/processed/fund_master_clean.csv")

# Category Distribution
plt.figure(figsize=(8,5))
fund_master["category"].value_counts().plot(kind="bar")
plt.title("Fund Category Distribution")
plt.tight_layout()
plt.savefig("reports/category_distribution.png")

# Risk Distribution
plt.figure(figsize=(8,5))
fund_master["risk_category"].value_counts().plot(kind="bar")
plt.title("Risk Category Distribution")
plt.tight_layout()
plt.savefig("reports/risk_distribution.png")

print("Visualizations Saved Successfully!")