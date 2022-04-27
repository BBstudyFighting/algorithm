-- 입양일이 잘못 입력돼 보호시작일(INS) 보다 입양일(OUTS)가 더 빠른 데이터 찾기
-- 둘 이상의 테이블을 연결하여 데이터를 검색하는 JOIN 활용

SELECT INS.ANIMAL_ID, INS.NAME -- INS의 ID와 NAME 찾기
FROM ANIMAL_INS INS JOIN ANIMAL_OUTS OUTS -- 두 데이터를 JOIN
WHERE INS.ANIMAL_ID = OUTS.ANIMAL_ID -- 두 테이블이 ID가 같고,
AND  INS.DATETIME > OUTS.DATETIME -- 보호시작이이 더 빠른 데이터를 
ORDER BY INS.DATETIME -- 보호시작일 기준으로 오름차순(디폴트) 정렬