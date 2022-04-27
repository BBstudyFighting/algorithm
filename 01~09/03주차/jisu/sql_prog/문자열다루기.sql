-- [문제출처 프로그래머스 SQL 고득점 키트](https://programmers.co.kr/learn/challenges)  
-- 문제의 저작권은 Programmers에게 있습니다.

-- ### 문제 및 풀이접근


-- ```python
-- STRING (문자열 다루기)
-- 1. 특정 이름의 동물 찾기 -> IN 활용 
-- 2. 이름에 'EL'이 들어간 Dog 찾기 -> LIKE % % 활용
-- 3. 중성화 여부 파악 -> IF & LIKE 활용
--     - SEX_UPDON_INTAKE 컬럼값에 
--       Neutered, Spayed 들어있으면 중성화된 것임  
--     - 중성화 됐으면 O 아니면 X 로 표시
-- ```

-- ### 코드

-- 루시와 엘라 찾기 (특정 이름의 동물 찾기)
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE 
FROM ANIMAL_INS -- IN 활용
WHERE NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
ORDER BY ANIMAL_ID

-- 이름에 EL이 들어가는 동물(멍멍이)찾기
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS -- LIKE 활용, 앞뒤 % 써서 위치상관없이 포함 확인
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME

-- 중성화 여부 파악하기 IF 활용
SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE -- 중성화 컬럼 O,X 표시하기 
LIKE '%NEUTERED%' OR SEX_UPON_INTAKE LIKE '%SPAYED%','O','X') 
AS '중성화' FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC
