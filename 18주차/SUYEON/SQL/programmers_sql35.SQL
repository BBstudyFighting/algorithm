# 조건별로 분류하여 주문상태 출력하기
SELECT order_id,product_id, 
    LEFT(out_date,10) AS OUT_DATE, 
    if(LEFT(out_date,10) <= '2022-05-01', '출고완료',if(out_date is null, '출고미정','출고대기')) as 출고여부
from food_order
order by order_id
-----------------------------------------------------
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') as OUT_DATE, 
    CASE
    WHEN DATE_FORMAT(OUT_DATE, '%m-%d') <= '05-01' THEN '출고완료'
    WHEN DATE_FORMAT(OUT_DATE, '%m-%d') > '05-01' THEN '출고대기'
    ELSE '출고미정' 
    END AS 출고여부
FROM FOOD_ORDER 
ORDER BY ORDER_ID ASC