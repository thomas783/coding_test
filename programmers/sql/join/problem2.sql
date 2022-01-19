-- 있었는데요 없었습니다

SELECT ins.animal_id, ins.name
FROM animal_ins AS ins INNER JOIN animal_outs AS outs
    ON ins.animal_id = outs.animal_id
WHERE ins.datetime > outs.datetime
ORDER BY ins.datetime;