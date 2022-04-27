-- Weather Observation Station 5
-- 길이가 가장 긴 도시, 짧은 도시를 1개씩 찾기
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) ASC, CITY ASC LIMIT 1;
-- 오름차순, 내림차순 SELECT 문 2개를 붙여준다.
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY ASC
LIMIT 1


-- Weather Observation Station 6
-- 'a','e','i','o','u'로 시작하는 도시 찾기
SELECT DISTINCT CITY FROM STATION
WHERE LEFT(CITY,1) IN ('a','e','i','o','u');

-- Weather Observation Station 7
-- 'a','e','i','o','u'로 끝나는 도시 찾기
SELECT DISTINCT CITY FROM STATION
WHERE RIGHT(CITY,1) IN ('a','e','i','o','u');

-- Weather Observation Station 8
-- 'a','e','i','o','u'로 시작하거나 끝나는 도시 찾기 
SELECT DISTINCT CITY FROM STATION
WHERE LEFT(CITY,1) IN ('a','e','i','o','u')
AND RIGHT(CITY,1) IN ('a','e','i','o','u');

-- Weather Observation Station 9
-- 모음으로 시작하지 않는 도시 찾기
SELECT DISTINCT CITY FROM STATION
WHERE LEFT(CITY,1) NOT IN ('a','e','i','o','u');

-- Weather Observation Station 10
-- 'a','e','i','o','u'로 끝나지 않는 도시 찾기
SELECT DISTINCT CITY FROM STATION
WHERE RIGHT(CITY,1) NOT IN ('a','e','i','o','u');

-- Weather Observation Station 11
-- 'a','e','i','o','u'로 시작하지 않거나 끝나지 않는 도시 찾기 
SELECT DISTINCT CITY FROM STATION
WHERE LEFT(CITY,1) NOT IN ('a','e','i','o','u')
OR RIGHT(CITY,1) NOT IN ('a','e','i','o','u');

-- Weather Observation Station 12
-- 'a','e','i','o','u'로 시작하지 않고, 끝나지 않는 도시 찾기 
SELECT DISTINCT CITY FROM STATION
WHERE LEFT(CITY,1) NOT IN ('a','e','i','o','u')
AND RIGHT(CITY,1) NOT IN ('a','e','i','o','u');
