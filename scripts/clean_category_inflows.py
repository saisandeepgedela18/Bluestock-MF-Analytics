import pandas as pd

df = pd.read_csv("data/raw/05_category_inflows.csv")

df = df.drop_duplicates()
df = df.dropna()

df.to_csv(
    "data/processed/category_inflows_clean.csv",
    index=False
)

print("Category Inflows Cleaned Successfully!")
print(df.shape)