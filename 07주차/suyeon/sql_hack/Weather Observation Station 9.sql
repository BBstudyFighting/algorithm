'''
Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
'''
SELECT DISTINCT city
FROM station
WHERE city not REGEXP '^[aeiou]'; # do not start with vowels.