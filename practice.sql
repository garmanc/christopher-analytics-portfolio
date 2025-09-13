SELECT product, quantity, price, quantity * price AS revenue
FROM sandbox.sales
WHERE region = 'West'
ORDER BY sale_date DESC
LIMIT 5;