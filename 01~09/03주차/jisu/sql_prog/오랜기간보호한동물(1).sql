-- 오랜기간 보호한 동물
-- 아직 입양을 못간 동물(OUTS.DATETIME -> NULL) 
-- INS.DATETIME이 가장 오래된 동물 3개 정렬

SELECT INS.NAME, INS.DATETIME -- INS의 이름과 보호시작일을 보여줌
FROM ANIMAL_INS INS LEFT JOIN ANIMAL_OUTS OUTS 
-- 왼쪽테이블을 기준으로 하는 LEFT JOIN
ON INS.ANIMAL_ID=OUTS.ANIMAL_ID
-- INS의 ID와 OUTS의 ID가 같은 것 중에
WHERE OUTS.DATETIME IS NULL -- 입양일이 NULL 인 데이터
ORDER BY INS.DATETIME -- 보호시작일 오름차순 정렬
LIMIT 3 -- 3개 제한