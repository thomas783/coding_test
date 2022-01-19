-- 없어진 기록 찾기

SELECT outs.animal_id,outs.name
FROM animal_ins AS ins RIGHT JOIN animal_outs AS outs
ON ins.animal_id = outs.animal_id
WHERE ins.datetime IS NULL
ORDER BY outs.animal_id, outs.name;