-- Write your PostgreSQL query statement below
select contest_id, Round(100.*count(distinct user_id)/(select count(*) from users),2) as percentage
from register
group by contest_id
order by percentage desc, contest_id