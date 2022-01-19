-- 중성화 여부 파악하기

SELECT animal_id, name,
    CASE 
        WHEN sex_upon_intake LIKE "%Spayed%"
        OR sex_upon_intake LIKE "%Neutered%"
        THEN 'O'
        ELSE 'X'
    END AS 중성화
FROM animal_ins
ORDER BY animal_id;