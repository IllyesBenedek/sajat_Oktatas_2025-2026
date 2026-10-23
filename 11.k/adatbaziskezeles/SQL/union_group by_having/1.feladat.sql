SELECT DISTINCT ship_state_province FROM orders
UNION 
SELECT DISTINCT state_province FROM customers;