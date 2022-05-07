'''
Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

where LAT_N is the northern latitude and LONG_W is the western longitude.
'''
SELECT distinct CITY
FROM STATION
WHERE CITY like '%a' or  CITY like '%e' or CITY like '%i' or CITY like '%o' or CITY like '%u' 

SELECT distinct CITY
FROM STATION
WHERE CITY REGEXP '[aeiou]$'
