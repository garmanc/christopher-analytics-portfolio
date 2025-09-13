SELECT product, quantity, price, quantity * price AS revenue
FROM sandbox.sales
WHERE region IN ('West', 'East');