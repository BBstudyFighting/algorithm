# https://www.hackerrank.com/

-- Weather Observation Station 5
SELECT city, CHAR_LENGTH(city)
FROM station
ORDER BY CHAR_LENGTH(city) ASC, city ASC
LIMIT 1;

SELECT city, CHAR_LENGTH(city)
FROM station
ORDER BY CHAR_LENGTH(city) DESC, city ASC
limit 1;

-- Weather Observation Station 6
SELECT DISTINCT city 
FROM station
WHERE (city LIKE "a%" OR city LIKE "e%" OR city LIKE "i%" OR city LIKE "o%" OR city LIKE "u%");
/* 정규표현식 사용 https://junyoung-developer.tistory.com/34?category=929724 참고
SELECT DISTINCT city 
FROM station
WHERE city REGEXP '^[aeiou]'; */

-- Weather Observation Station 7
SELECT DISTINCT city
FROM station
WHERE city REGEXP '[aeiou]$';
/*
SELECT DISTINCT city 
FROM station
WHERE (city LIKE "%a" OR city LIKE "%e" OR city LIKE "%i" OR city LIKE "%o" OR city LIKE "%u"); */

-- Weather Observation Station 8
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[aeiou]' AND city REGEXP '[aeiou]$';

-- Weather Observation Station 9
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[^aeiou]';

-- Weather Observation Station 10
SELECT DISTINCT city
FROM station
WHERE city REGEXP '[^aeiou]$';
