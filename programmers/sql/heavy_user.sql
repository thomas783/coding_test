-- 헤비 유저가 소유한 장소

SELECT id, name, host_id
FROM places
WHERE host_id in
    (SELECT host_id
    FROM places
    GROUP BY host_id
    HAVING COUNT(host_id) >= 2)
ORDER BY id;