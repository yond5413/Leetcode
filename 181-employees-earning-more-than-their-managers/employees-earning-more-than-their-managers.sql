-- Write your PostgreSQL query statement below
select a.name as Employee
from employee a
left join employee b on a.managerId = b.id
where a.salary >b.salary