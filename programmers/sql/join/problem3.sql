-- 오랜 기간 보호한 동물(1)

SELECT ins.name, ins.datetime
FROM animal_ins AS ins LEFT OUTER JOIN animal_outs AS outs
ON ins.animal_id = outs.animal_id
WHERE outs.datetime IS NULL
ORDER BY ins.datetime
LIMIT 3;