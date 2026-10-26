select category, AVG(list_price) FROM products
GROUP BY category HAVING AVG(list_price) > 40;