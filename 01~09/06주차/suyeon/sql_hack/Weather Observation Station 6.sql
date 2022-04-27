'''
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
'''
SELECT City
FROM Station
WHERE City LIKE 'A%' or City LIKE 'E%' or City LIKE 'I%' or City LIKE 'O%' or City LIKE 'U%';
