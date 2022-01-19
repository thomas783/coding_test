-- 입양 시각 구하기(1)

SELECT HOUR(datetime) AS hour, COUNT(animal_id) AS count
FROM animal_outs
GROUP BY hour
HAVING hour BETWEEN 9 AND 19
ORDER BY hour;