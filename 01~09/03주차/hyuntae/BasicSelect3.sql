# https://www.hackerrank.com/

-- Weather Observation Station 11
SELECT DISTINCT city 
FROM station
WHERE city REGEXP '^[^aeiou]' OR city REGEXP '[^aeiou]$';

-- Weather Observation Station 12
SELECT DISTINCT city 
FROM station
WHERE city REGEXP '^[^aeiou]' AND city REGEXP '[^aeiou]$';

-- Higher Than 75 Marks
SELECT name
FROM students
WHERE marks > 75
ORDER BY RIGHT(name, 3), ID ASC;

-- Employee Names
SELECT name
FROM employee
ORDER BY name ASC;

-- Employee Salaries
SELECT name
FROM employee
WHERE salary > 2000 AND months <10
ORDER BY employee_id ASC;