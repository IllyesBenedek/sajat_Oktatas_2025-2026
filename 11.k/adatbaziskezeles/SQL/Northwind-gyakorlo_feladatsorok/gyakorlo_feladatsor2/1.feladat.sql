SELECT product_name, list_price FROM products
WHERE list_price > 15 AND discontinued = 0
AND category <> 'Condiments' ORDER BY list_price ASC;