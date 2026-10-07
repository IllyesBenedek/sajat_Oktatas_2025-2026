use northwind;

select COUNT(id) from employees where city = "Seattle";
select COUNT(id) from employees where job_title = "Sales Representativ";
select COUNT(id) from employees where first_name like 'A%';
