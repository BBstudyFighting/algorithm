'''
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
'''
SELECT CITY
FROM STATION
WHERE CITY like 'a%' or  CITY like 'e%' or CITY like 'i%' or CITY like 'o%' or CITY like 'u%' 

SELECT CITY
FROM STATION
WHERE CITY regexp '^[a,e,i,o,u]'