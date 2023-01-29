# 자동차 대여 기록 별 대여 금액 구하기
SELECT HISTORY_ID AS HISTORY_ID,
    ROUND((DAILY_FEE * (100 - IFNULL(DISCOUNT_RATE, 0)) /100) * PERIOD) AS FEE
FROM (
    SELECT *,
        TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 AS PERIOD,
        CASE WHEN TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 90 THEN '90일 이상'
            WHEN TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 30 THEN '30일 이상'
            WHEN TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 7 THEN '7일 이상'
            ELSE '7일 미만' END AS DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    JOIN CAR_RENTAL_COMPANY_CAR C USING (CAR_ID)) A
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
USING (CAR_TYPE, DURATION_TYPE)
WHERE CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC
----------------------------------------------------------------------------------------
SELECT HISTORY_ID,
ROUND(CASE 
      WHEN HIS.DURATION < 7 THEN REN.DAILY_FEE * HIS.DURATION

      WHEN HIS.DURATION < 30 THEN REN.DAILY_FEE * HIS.DURATION *
                            (SELECT 1 - DISCOUNT_RATE/100 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '7일 이상')

      WHEN HIS.DURATION < 90 THEN REN.DAILY_FEE * HIS.DURATION *
                            (SELECT 1 - DISCOUNT_RATE/100 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '30일 이상')

      ELSE REN.DAILY_FEE * HIS.DURATION *
                            (SELECT 1 - DISCOUNT_RATE/100 FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE CAR_TYPE = '트럭' AND DURATION_TYPE = '90일 이상') END) FEE

FROM (SELECT HISTORY_ID,CAR_ID,(DATEDIFF(END_DATE,START_DATE)+1) DURATION 
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) HIS 
JOIN CAR_RENTAL_COMPANY_CAR REN 
ON HIS.CAR_ID = REN.CAR_ID
WHERE REN.CAR_TYPE = '트럭'
ORDER BY FEE DESC,HISTORY_ID DESC;
----------------------------------------------------------------------------------------
#  자동차 대여기록 기준으로 사용 기간과 요금을 한테이블로 결합

with truck AS (
        SELECT a.history_id AS HISTORY_ID
            , a.car_id
            , b.car_type
            , b.daily_fee
            , DATEDIFF(end_date, start_date)+1 as daydiff
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY  a
            LEFT JOIN CAR_RENTAL_COMPANY_CAR b ON a.car_id = b.car_id
            )
            
# 할인율 적용 7일 이상 5% / 30일 이상 8% / 90일 이상 15% 

SELECT HISTORY_ID
    , ROUND(CASE WHEN daydiff < 7 THEN daily_fee*daydiff
                 WHEN daydiff < 30 THEN (daily_fee-(daily_fee*0.05))*daydiff
                 WHEN daydiff < 90 THEN (daily_fee-(daily_fee*0.08))*daydiff 
                 ELSE (daily_fee-(daily_fee*0.15))*daydiff END,0)  AS FEE 
FROM truck
WHERE car_type ='트럭'
ORDER BY FEE DESC , HISTORY_ID DESC
-- 굳이 결합할 필요가 없는경우, 필요한 정보만 간단히 메모해놓자.
-- 할인율 정보가 들어간 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블의 경우 굳이 JOIN시킬 필요가 없고 '트럭'에 해당하는 할인조건만 뽑아서 메모해도 됬었습니다. 시나리오 과정을 요약하면 다음과 같습니다.
-- 자동차 대여기록(HISTORY) 기준으로 사용 기간(daydiff)과 요금(daily_fee)을 한테이블로 결합 (PK:car_id)
-- 트럭에 해당하는 차만 뽑아서 문제에서 제시된 할인율을 적용