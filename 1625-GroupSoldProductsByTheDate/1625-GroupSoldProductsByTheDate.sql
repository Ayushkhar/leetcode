-- Last updated: 6/6/2026, 10:24:45 PM
# Write your MySQL query statement below
with cte as
(
    select sell_date
         , count(distinct product) as num_sold
         , group_concat(distinct product order by product) as products
    from Activities 
    group by sell_date
)
select * from cte order by sell_date