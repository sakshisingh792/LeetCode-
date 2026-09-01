# Write your MySQL query statement below

select product_name ,year,price from sales as a left JOIN  product as p
on a.product_id=p.product_id;