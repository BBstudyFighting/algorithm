# 식품분류별 가장 비싼 식품의 정보 조회하기
SELECT food.category AS CATEGORY
    , food.price AS MAX_PRICE
    , food.product_name AS PRODUCT_NAME
FROM food_product AS food
WHERE food.category IN ('과자','국','김치','식용유')
    AND food.price IN (SELECT MAX(price) FROM food_product
                    GROUP BY category)
ORDER BY food.price DESC

SELECT FP1.CATEGORY, FP1.PRICE AS MAX_PRICE, FP1.PRODUCT_NAME
FROM FOOD_PRODUCT AS FP1 INNER JOIN 
    (SELECT CATEGORY, MAX(PRICE) AS PRICE
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY)
    AS FP2
WHERE FP1.CATEGORY = FP2.CATEGORY AND FP1.PRICE = FP2.PRICE AND FP1.CATEGORY IN ("과자", "국", "김치", "식용유")
ORDER BY MAX_PRICE DESC