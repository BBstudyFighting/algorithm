#1 상위 n개 레코드
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1

#2 최댓값 구하기
SELECT MAX(DATETIME)
FROM ANIMAL_INS

#3 최솟값 구하기
SELECT MIN(DATETIME)
FROM ANIMAL_INS