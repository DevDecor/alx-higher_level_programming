-- Select duplicate
SELECT score, COUNT(*) AS number
GROUP BY score
ORDER BY score DESC;
