USE northwind;

SELECT product_name, list_price FROM products WHERE list_price > 20 AND discontinued = 0 AND NOT category = 'Beverages' ORDER BY list_price ASC;

SELECT last_name, first_name, job_title FROM employees ORDER BY job_title DESC;

SELECT  product_name, MAX(list_price) FROM products;
SELECT  product_name, MIN(list_price) FROM products;
SELECT  product_name, AVG(list_price) FROM products;
SELECT  product_name, SUM(list_price) FROM products;

SELECT COUNT(*),job_title FROM employees GROUP BY job_title;

SELECT category, AVG(list_price) FROM products GROUP BY category HAVING AVG(list_price) > 50;

SELECT first_name, last_name, city FROM customers 
UNION
SELECT first_name, last_name, city FROM employees;



DROP DATABASE IF EXISTS repter;
CREATE DATABASE repter;
USE repter;

CREATE TABLE gepek(
    gep_id INT AUTO_INCREMENT PRIMARY KEY,
    tipus NOT NULL,
    ferohely INT DEFAULT(100)
);

CREATE TABLE jaratok(
    jarat_id INT AUTO_INCREMENT PRIMARY KEY,
    celallomas VARCHAR(50) INT,
    FOREIGN KEY(gepek) REFERENCES (gep_id)
);
