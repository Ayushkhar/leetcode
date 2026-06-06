-- Last updated: 6/6/2026, 10:25:27 PM
# Write your MySQL query statement below
with sub_grt5 as 
(
    select class,count(class) as class_count 
    from Courses 
    group by class
    having count(class)>=5
)
select class from sub_grt5 