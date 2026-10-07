use northwind;

select SUM(standard_cost) from products;
select SUM(standard_cost) from products WHERE list_price BETWEEN 20 and 50;
select SUM(standard_cost) from products where NOT category = "Sauces";
