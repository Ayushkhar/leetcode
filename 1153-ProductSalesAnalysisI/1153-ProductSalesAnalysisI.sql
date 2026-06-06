-- Last updated: 6/6/2026, 10:25:00 PM
# Write your MySQL query statement below
select product_name,year,price from Sales s 
inner join Product p 
on s.product_id = p.product_id
