-- Write your PostgreSQL query statement below
select u.unique_id,e.name 
from Employees e
left join EmployeeUni u on u.id = e.id