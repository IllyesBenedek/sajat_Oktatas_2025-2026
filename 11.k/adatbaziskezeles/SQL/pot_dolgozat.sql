SELECT product_name, list_price, category FROM products WHERE list_price < 40 OR category = 'Dried Fruit & Nuts' ORDER BY list_price DESC;

SELECT job_title, first_name, last_name FROM employees ORDER BY last_name ASC, first_name DESC;

SELECT  MAX(shipping_fee) FROM orders;
SELECT MIN(shipping_fee) FROM orders;
SELECT AVG(shipping_fee) FROM orders;
SELECT SUM(shipping_fee) FROM orders;
SELECT shipped_date, COUNT(*) FROM orders;

SELECT payment_type, COUNT(*) FROM orders GROUP BY payment_type ;

SELECT category, AVG(list_price) FROM products GROUP BY category HAVING AVG(list_price) > 19;

SELECT company, city FROM customers
UNION
SELECT company, city FROM shippers;

DROP DATABASE if EXISTS muhely;
CREATE DATABASE muhely;
use muhely;

CREATE table gepjarmuvek(
    gepjarmuvek_id INT AUTO_INCREMENT PRIMARY KEY,
    tipus INT VARCHAR(20)  NOT NULL DEFAULT(Toyota),
    modell INT VARCHAR(20),
    rendszam_id INT VARCHAR(15),
    ajtok_szama INT CHECK(4),
    gyartas_eve INT DATA
);
  
CREATE table autok(
    tipus Opel,
    modell Polski Fiat,
    rendszam ASS-MAN69,
    autoinak_szama 2,
    gyartasi_datum 2003
);
