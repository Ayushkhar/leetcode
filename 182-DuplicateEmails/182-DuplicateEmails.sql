-- Last updated: 6/6/2026, 10:26:24 PM
# Write your MySQL query statement below
with cte(email,countt) as 
(
    select email,count(email) as countt 
    from Person 
    group by email 
)
select email from cte where countt> 1