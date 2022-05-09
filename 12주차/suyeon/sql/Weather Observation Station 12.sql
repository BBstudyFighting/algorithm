'''
Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
'''
SELECT distinct CITY
FROM STATION
WHERE CITY not REGEXP '^[aeiou]' and CITY not REGEXP '[aeiou]$'