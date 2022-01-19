-- 입양 시각 구하기(2)

SET @hour = -1;
SELECT (@hour := @hour + 1) AS hour,
    (SELECT COUNT(HOUR(datetime))
    FROM animal_outs
    WHERE HOUR(datetime) = @hour) AS count
    FROM animal_outs
WHERE @hour < 23;