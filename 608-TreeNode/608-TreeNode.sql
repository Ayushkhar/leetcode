-- Last updated: 6/6/2026, 10:25:26 PM
# Write your MySQL query statement below
with ParentNodes AS (
    select DISTINCT p_id
    from Tree
    WHERE p_id IS not NULL
)
select t.id,
       CASE
           WHEN t.p_id IS NULL THEN 'Root'
           when pn.p_id IS not null then 'Inner'
           ELSE 'Leaf'
       END AS type
FROM Tree t
LEFT join ParentNodes pn
       ON t.id = pn.p_id;