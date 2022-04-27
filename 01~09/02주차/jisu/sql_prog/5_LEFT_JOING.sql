-- 없어진 기록 찾기

-- 들어온 기록(INS)에 없는데 나간 기록(OUTS)은 있는 데이터를 찾는 쿼리
-- OUTS에 있는 ID와 NAME 데이터를 출력하는데, 
SELECT OUTS.ANIMAL_ID, OUTS.NAME
-- OUTS ID 를 기준으로 INS ID 가 일치하는 데이터는 가져오지만 
FROM ANIMAL_OUTS OUTS 
    LEFT JOIN ANIMAL_INS INS ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
-- 없는 데이터는 NULL 로 표시되게 된다
WHERE INS.ANIMAL_ID IS NULL
ORDER BY OUTS.ANIMAL_ID
