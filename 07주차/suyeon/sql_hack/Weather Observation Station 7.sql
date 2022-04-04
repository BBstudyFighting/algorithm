'''
Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

where LAT_N is the northern latitude and LONG_W is the western longitude.
'''
SELECT DISTINCT city # 중복안됨
FROM station
WHERE city
LIKE ('%a') OR CITY LIKE ('%e') OR CITY LIKE ('%i')OR CITY LIKE ('%o')OR CITY LIKE ('%u'); # ending

# 정규 표현식
SELECT DISTINCT city
FROM station
WHERE city REGEXP '[aeiou]$';