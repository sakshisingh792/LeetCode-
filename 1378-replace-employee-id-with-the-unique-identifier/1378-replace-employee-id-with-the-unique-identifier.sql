# Write your MySQL query statement below
select unique_id , name
from employees as a 
left join employeeuni as eu
on a.id=eu.id
