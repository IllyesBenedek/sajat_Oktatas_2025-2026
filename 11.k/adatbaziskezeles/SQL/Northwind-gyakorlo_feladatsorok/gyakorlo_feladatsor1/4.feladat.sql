-- SQLBook: Code
SELECT ship_city, COUNT(*) AS rendelések_szama FROM orders GROUP BY ship_city;