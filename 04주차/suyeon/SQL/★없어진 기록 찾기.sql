'''
천재지변으로 인해 일부 데이터가 유실되었습니다. 
입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.


입양 OUT 기록은 있는데 입양 IN 기록이 없는 동물 찾기
입양 OUT과 입양IN을 연결 : LEFT OUTER JOIN (KEY는 ANIMAL_ID)
입양 OUT 목록은 다 나와야 하는데 입양 IN 목록에 값이 있으면 나오고, 없으면 NULL이 출력됨
입양 IN 목록에 없는 동물 찾기
입양 IN 의 ANIMAL_ID가 NULL인 값을 찾기 : WHIERE IN.ANIMAL_ID IS NULL
ID 순으로 출력 : ORDER BY 

'''
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS LEFT JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY OUTS.ANIMAL_ID ASC;
