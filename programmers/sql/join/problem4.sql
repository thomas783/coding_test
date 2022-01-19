-- 보호소에서 중성화한 동물

SELECT ins.animal_id, ins.animal_type, ins.name
FROM animal_ins AS ins INNER JOIN animal_outs AS outs
    ON ins.animal_id = outs.animal_id
WHERE (ins.sex_upon_intake NOT LIKE "%Spayed%" 
    AND ins.sex_upon_intake NOT LIKE "%Neutered%")
    AND (outs.sex_upon_outcome LIKE "%Spayed%"
    OR outs.sex_upon_outcome LIKE "%Neutered%")
ORDER BY ins.animal_id;