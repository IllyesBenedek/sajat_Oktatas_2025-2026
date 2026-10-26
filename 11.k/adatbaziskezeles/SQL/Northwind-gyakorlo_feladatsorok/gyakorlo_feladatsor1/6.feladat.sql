SELECT first_name, last_name, city FROM customers
UNION
SELECT first_name, last_name, city FROM employees;