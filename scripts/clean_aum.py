import pandas as pd

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Remove duplicates
df = df.drop_duplicates()

# Remove nulls
df = df.dropna()

# Save cleaned file
df.to_csv(
    "data/processed/aum_by_fund_house_clean.csv",
    index=False
)

print("AUM Cleaned Successfully!")
print(df.shape)
