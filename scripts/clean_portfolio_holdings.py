import pandas as pd

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

df = df.drop_duplicates()
df = df.dropna()

df.to_csv(
    "data/processed/portfolio_holdings_clean.csv",
    index=False
)

print("Portfolio Holdings Cleaned Successfully!")
print(df.shape)