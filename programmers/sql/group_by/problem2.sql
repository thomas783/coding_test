-- 동명 동물 수 찾기

SELECT name, COUNT(animal_id) AS count
FROM animal_ins
WHERE name IS NOT NULL
GROUP BY name
HAVING count > 1
ORDER BY name;