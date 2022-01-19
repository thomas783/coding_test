-- 이름에 el이 들어가는 동물 찾기

SELECT animal_id, name
FROM animal_ins
WHERE name LIKE "%el%"
    AND animal_type = "dog"
ORDER BY name;