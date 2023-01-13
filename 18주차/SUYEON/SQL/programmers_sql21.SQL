# 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
SELECT car_type ,COUNT(car_id) AS CARS 
FROM car_rental_company_car
WHERE options LIKE '%시트%'
GROUP BY car_type
ORDER BY car_type ASC

SELECT CAR_TYPE, COUNT(car_id) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE options REGEXP '통풍시트|열선시트|가죽시트'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC