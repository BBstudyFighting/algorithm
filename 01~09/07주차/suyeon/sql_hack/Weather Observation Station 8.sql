'''
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

where LAT_N is the northern latitude and LONG_W is the western longitude.
'''
# 실패한 코드
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[aeiou]$'; # 안돌아감

#성공한 코드 1
SELECT DISTINCT city
FROM station
WHERE city REGEXP '[aeiou]$'and city REGEXP '^[aeiou]'

#성공한 코드 2 : 너무 길어서 비효율적인듯..
select distinct city from station
where (city like 'a%'
or city like 'e%'
or city like 'i%'
or city like 'o%'
or city like 'u%')
and
(
city like '%a'
or city like '%e'
or city like '%i'
or city like '%o'
or city like '%u'
)

#성공한 코드 3
SELECT DISTINCT(CITY) 
FROM STATION 
WHERE SUBSTR(CITY, 1, 1) IN ('a', 'e', 'o', 'i', 'u') and SUBSTR(CITY, -1, 1) IN ('a', 'e', 'o', 'i', 'u')

-- SUBSTR(문자열, 시작 위치, 가져올 문자 길이)
-- SUBSTR(CITY, 1, 1) : CITY 데이터에서 첫 번째 글자
-- SUBSTR(CITY, -1, 1) : CITY 데이터에서 마지막 글자
-- SUBSTR(CITY, -3, 3) : 뒤에서 세 번째부터 세 글자
