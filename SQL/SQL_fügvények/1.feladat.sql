use northwind;

select AVG(standard_cost) from products;
select AVG(standard_cosc) from products where list_price < 30;
select AVG(standard_cost) from products where category = "Sauces";
