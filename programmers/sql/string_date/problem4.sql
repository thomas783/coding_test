-- 오랜 기간 보호한 동물(2)

SELECT ins.animal_id, ins.name
FROM animal_outs AS outs INNER JOIN animal_ins as ins
ON outs.animal_id = ins.animal_id
ORDER BY outs.datetime - ins.datetime DESC
LIMIT 2;