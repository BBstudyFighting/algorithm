-- [문제출처 프로그래머스 SQL 고득점 키트](https://programmers.co.kr/learn/challenges)  
-- 문제의 저작권은 Programmers에게 있습니다.

-- ### 문제 및 풀이접근

-- DATE(날짜) 다루기
-- 1. DATE 타입끼리 연산 가능
-- 2. DATE_FORMAT 으로 형식 변경 가능

-- ### 코드

-- 오랜기간 보호한 동물(2)
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_INS INS, ANIMAL_OUTS OUTS
WHERE INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY OUTS.DATETIME - INS.DATETIME DESC 
-- 입양일 - 보호시작일 하고, 
-- 내림차순하면 차이 큰(오래된) 순으로 정렬됨
LIMIT 2 

-- DATETIME에서 DATE 형 변환
SELECT ANIMAL_ID, NAME, 
DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
-- DATE_FORMAT 으로 형식 변경
FROM ANIMAL_INS

