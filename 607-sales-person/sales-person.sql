-- Write your PostgreSQL query statement below
select s.name 
from SalesPerson s
where s.sales_id not in
(
    select o.sales_id
    from company c
    join orders o on o.com_id = c.com_id
    where c.name = 'RED'
)