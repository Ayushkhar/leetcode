-- Last updated: 6/6/2026, 10:26:23 PM
# Write your MySQL query statement below
select Customers.name as Customers
from Customers 
left outer join Orders 
on Customers.id = Orders.customerId
where Orders.id is NULL