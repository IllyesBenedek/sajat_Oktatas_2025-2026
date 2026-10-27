SELECT category, AVG(list_price)AS atlagos_lista_ar FROM products
GROUP BY category
HAVING AVG(list_price) > 45;