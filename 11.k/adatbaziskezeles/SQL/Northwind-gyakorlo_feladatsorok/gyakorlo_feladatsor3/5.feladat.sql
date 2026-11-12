SELECT category, AVG(list_price)AS atlagos_ar FROM products
GROUP BY category HAVING AVG(list_price) > 35;