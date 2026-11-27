USE northwind;

SELECT product_name, list_price FROM products WHERE list_price < 60 AND discontinued = 0 AND NOT category = 'Beverages'  ORDER BY list_price DESC;


SELECT first_name, last_name, job_title FROM employees ORDER BY last_name DESC, first_name ASC;


SELECT product_name, MIN(list_price) FROM products;

SELECT product_name, MAX(list_price) FROM products;

SELECT product_name, AVG(list_price) FROM products;

SELECT product_name, SUM(list_price) FROM products;


SELECT COUNT(*), ship_city FROM orders GROUP BY ship_city; 


SELECT product_name, AVG(list_price)  FROM products GROUP BY category HAVING AVG(list_price) > 35;


SELECT first_name, last_name, city FROM customers
UNION
SELECT first_name, last_name, city FROM employees;


DROP DATABASE IF EXISTS etterem;
CREATE DATABASE etterem;

CREATE table etelek(
    etel_id INT PRIMARY KEY AUTO_INCREMENT,
    etel_nev VARCHAR(80) NOT NULL,
    ar INT DEFAULT(1500)
);

CREATE TABLE rendelesek(
    rendeles_id INT PRIMARY KEY AUTO_INCREMENT,
    rendeles_nev VARCHAR(60),
    etel_id INT,
    FOREIGN KEY(etel_id) REFERENCES etelek (etel_id)
);


SELECT product_name, list_price FROM products WHERE list_price > 15 AND discontinued = 0 AND NOT category = 'Condiments' ORDER BY list_price ASC;
