-- Write your PostgreSQL query statement below
select d.name as department, e.name as employee, max(e.salary) as salary
from employee e
join department d on d.id = e.departmentId
where (e.departmentId,e.salary)  in (
    select departmentId, max(salary)
    from employee
    group by departmentId
)
group by d.name,e.name, e.salary
order by e.salary desc
/*
group by d.name,e.name, e.salary
order by e.salary desc
*/