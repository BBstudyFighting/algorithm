# https://www.hackerrank.com/

-- Select All
SELECT *
FROM CITY;

-- Weather Observation Station 1
SELECT CITY, STATE
FROM STATION;

-- Weather Observation Station 3
SELECT DISTINCT city
FROM station
WHERE (ID % 2) = 0;

-- Weather Observation Station 4
# SET
SET @A = (SELECT COUNT(*) FROM station);
SET @B = (SELECT COUNT(DISTINCT(city)) FROM station);
SELECT @A-@B;