from sqlalchemy import create_engine
import pandas as pd

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
fund_master = pd.read_csv(
    "data/processed/fund_master_clean.csv"
)

nav_history = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

investor_transactions = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

scheme_performance = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

# Load into SQLite
fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

investor_transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

scheme_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Database Loaded Successfully!")