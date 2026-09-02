# Write your MySQL query statement below
select id from(select id,recorddate,temperature ,
lag(temperature)over(order by recorddate) as prev_temp,
lag(recorddate)over(order by recorddate) as prev_date
from weather) as t
where temperature>prev_temp and datediff(recorddate,prev_date)=1;