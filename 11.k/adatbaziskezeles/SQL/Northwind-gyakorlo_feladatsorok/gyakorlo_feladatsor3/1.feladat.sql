select product_name, list_price FROM products 
WHERE list_price < 60 AND discontinued = 0
AND category <> 'Beverages' ORDER BY list_price DESC;