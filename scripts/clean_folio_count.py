import pandas as pd

df = pd.read_csv("data/raw/06_industry_folio_count.csv")

df = df.drop_duplicates()
df = df.dropna()

df.to_csv(
    "data/processed/industry_folio_count_clean.csv",
    index=False
)

print("Industry Folio Count Cleaned Successfully!")
print(df.shape)