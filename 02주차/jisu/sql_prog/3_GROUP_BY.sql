-- 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE

-- 동명 동물수 찾기
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
GROUP BY NAME HAVING COUNT(NAME) > 1
ORDER BY NAME;

-- 입양 시각 구하기 (1)
SELECT HOUR(DATETIME) HOUR, COUNT(DATETIME) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
HAVING HOUR >= 9 and HOUR <=19
ORDER BY HOUR(DATETIME)

-- 입양 시각 구하기(2)
-- 갑자기 난이도 상승 (로컬변수 활용)
SET @hour := -1;

SELECT (@hour := @hour + 1) as HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23

-- SET 옆 변수명과 초기값을 설정
-- @가 붙으면 로컬변수 프로시저가 끝나도 계속 유지, 
-- 0~23까지 누적하기 위해 활용
-- ':='은 비교 연산자 =과 구별하기 위한 대입 연산자
-- SELECT (@hour := @hour +1)로  @hour의 값이 1씩 증가
-- @hour 초기값이 -1 인데, 이 식으로 +1 이 되어 0 부터 시작
-- WHERE @hour < 23일 때까지, @hour 값이 계속 + 1씩 증가