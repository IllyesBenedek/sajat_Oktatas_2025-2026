SELECT first_name, last_name, city from customers
UNION
SELECT first_name, last_name, city FROM employees;