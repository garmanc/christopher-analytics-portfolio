SELECT quatity * price
FROM sandbox.sales
WHERE region = 'West', 'East'
ORDER BY sales_date
LIMIT ALL;