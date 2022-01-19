-- 우유와 요거트가 담긴 장바구니

SELECT DISTINCT(cart_id)
FROM cart_products
WHERE cart_id IN
    (SELECT cart_id
    FROM cart_products
    WHERE name = 'Yogurt')
    AND cart_id IN
    (SELECT cart_id
    FROM cart_products
    WHERE name = 'Milk')
ORDER BY cart_id;