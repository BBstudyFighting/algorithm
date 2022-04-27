-- [문제출처 HACKER RANK]
-- (https://www.hackerrank.com/domains/sql)  
-- 문제의 저작권은 해커랭크에 있습니다.


-- SELECT QUERY (1)
SELECT * FROM CITY
WHERE POPULATION >= 100000
AND CountryCode = 'USA'

-- SELECT QUERY (2)
SELECT NAME FROM CITY
WHERE POPULATION >= 120000
AND COUNTRYCODE = 'USA'

-- SELECT ALL
SELECT * FROM CITY

-- SELECT BY ID
SELECT * FROM CITY 
WHERE ID = '1661'

-- Japanese Cities' Attributes
SELECT * FROM CITY 
WHERE COUNTRYCODE = 'JPN'

-- Japanese Cities' Names
SELECT NAME FROM CITY 
WHERE COUNTRYCODE = 'JPN'

-- Weather Observation Station 1
SELECT CITY, STATE FROM STATION 

-- Weather Observation Station 3
-- ID가 even number(짝수)인 데이터 조회
-- exclude duplicates (중복제거) 
SELECT DISTINCT CITY FROM STATION 
WHERE (ID % 2) = 0 

-- Weather Observation Station 4
-- 총 CITY 항목수 - 고유 CITY 항목수
-- COUNT 활용 
SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION;
