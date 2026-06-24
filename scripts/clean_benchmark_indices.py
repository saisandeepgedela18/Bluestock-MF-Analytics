import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

df = df.drop_duplicates()
df = df.dropna()

df.to_csv(
    "data/processed/benchmark_indices_clean.csv",
    index=False
)

print("Benchmark Indices Cleaned Successfully!")
print(df.shape)