use northwind;

select MIN(standard_cost) from products;
select MAX(standard_cost) from products;
select max(standard_cost) from products WHERE product_code = 'CO';
