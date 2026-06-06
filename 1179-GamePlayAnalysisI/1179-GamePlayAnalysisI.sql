-- Last updated: 6/6/2026, 10:24:58 PM
# Write your MySQL query statement below
select player_id, min(event_date)as first_login from activity group by player_id;