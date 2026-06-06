-- Last updated: 6/6/2026, 10:24:49 PM
# Write your MySQL query statement below
select unique_id,name from Employees
left join EmployeeUNI 
on Employees.id=EmployeeUNI.id