SELECT product_name, list_price FROM products
WHERE list_price > 25 AND discontinued = 0
AND category <> 'Seafood'
ORDER BY list_price DESC;