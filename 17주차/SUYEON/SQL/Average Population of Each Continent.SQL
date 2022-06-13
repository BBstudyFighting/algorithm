'도시와 나라 테이블에서 각 대륙에 해당하는 도시들의 인구수 평균을 구하는 문제'
SELECT COUNTRY.Continent, TRUNCATE(AVG(CITY.Population),0) # 정수 아래자리까지 버림
FROM COUNTRY
JOIN CITY ON COUNTRY.CODE = CITY.COUNTRYCODE
GROUP BY COUNTRY.Continent