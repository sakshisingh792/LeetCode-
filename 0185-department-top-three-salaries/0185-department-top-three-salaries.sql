# Write your MySQL query statement below
SELECT D.name as Department, e.name as Employee, e.salary as Salary
FROM(
    SELECT e.*,
    Dense_rank() Over(partition by departmentId order by salary desc ) as rnk
    from employee e
)
e
JOIN  Department D 
ON e.departmentId=D.id
where rnk<=3;