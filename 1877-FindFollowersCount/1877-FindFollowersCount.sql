-- Last updated: 6/6/2026, 10:24:39 PM
SELECT user_id, COUNT(follower_id) AS followers_count
FROM followers
GROUP BY user_id
ORDER BY user_id 
