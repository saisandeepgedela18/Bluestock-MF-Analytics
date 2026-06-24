# Data Dictionary

## fund_master_clean.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| scheme_name | Text | Mutual Fund Scheme Name |
| fund_house | Text | Asset Management Company |
| category | Text | Fund Category |
| sub_category | Text | Fund Sub Category |

---

## nav_history_clean.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Fund Identifier |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## investor_transactions_clean.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | Text | Investor Identifier |
| transaction_date | Date | Transaction Date |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction Amount |

---

## scheme_performance_clean.csv

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | Float | One Year Return |
| return_3yr_pct | Float | Three Year Return |
| expense_ratio_pct | Float | Expense Ratio |