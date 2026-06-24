-- 1 Top 5 funds by AUM
SELECT fund_house, aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3 Average NAV per AMFI Code
SELECT amfi_code, AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

-- 4 Total Transactions by Type
SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 5 Transactions by State
SELECT state,
SUM(amount_inr)
FROM fact_transactions
GROUP BY state
ORDER BY SUM(amount_inr) DESC;

-- 6 Funds with Expense Ratio < 1%
SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 7 Top 5 Returns (1 Year)
SELECT scheme_name,
return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 8 Average Expense Ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- 9 Total AUM by Fund House
SELECT fund_house,
SUM(aum_crore)
FROM fact_aum
GROUP BY fund_house;

-- 10 Number of Schemes by Fund House
SELECT fund_house,
SUM(num_schemes)
FROM fact_aum
GROUP BY fund_house;