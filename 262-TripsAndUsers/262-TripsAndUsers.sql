-- Last updated: 6/6/2026, 10:26:03 PM
select
    t.request_at AS Day,
    ROUND(SUM(IF(t.status <> 'completed', 1, 0)) / COUNT(*), 2) AS 'Cancellation Rate'
from Trips t
where 
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND t.client_id not in (
        SELECT users_id FROM Users WHERE banned = 'Yes'
    )
    and t.driver_id NOT IN (
        select users_id FROM Users WHERE banned = 'Yes'
    )
GROUP BY t.request_at;
