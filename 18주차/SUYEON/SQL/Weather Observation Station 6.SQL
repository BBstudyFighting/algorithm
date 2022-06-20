SELECT CITY
FROM STATION
WHERE CITY regexp '^[A,E,I,O,U]'

SELECT CITY
FROM STATION
WHERE CITY like 'a%' or  CITY like 'e%' or CITY like 'i%' or CITY like 'o%' or CITY like 'u%' 