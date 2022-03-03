-- 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
FROM ANIMAL_INS
group by ANIMAL_TYPE 
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

-- SET 옆에 변수명과 초기값을 설정할 수 있습니다.
-- @가 붙은 변수는 프로시저가 종료되어도 유지된다고 생각하면 됩니다.
-- 이를 통해 값을 누적하여 0부터 23까지 표현할 수 있습니다.
-- @hour은 초기값을 -1로 설정합니다. PL/-SQL 문법에서 :=은 비교 연산자 =과 혼동을 피하기 위한의 대입 연산입니다.
-- SELECT (@hour := @hour +1) 은 @hour의 값에 1씩 증가시키면서 SELECT 문 전체를 실행하게 됩니다.
-- 이 때 처음에 @hour 값이 -1 인데, 이 식에 의해 +1 이 되어 0이 저장됩니다.
-- HOUR 값이 0부터 시작할 수 있습니다.
-- WHERE @hour < 23일 때까지, @hour 값이 계속 + 1씩 증가합니다.