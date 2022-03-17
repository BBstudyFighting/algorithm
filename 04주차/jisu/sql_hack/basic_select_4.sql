-- Higher Than 75 Marks
-- Marks 가 75 보다 높은 학생을 조회하시오
-- 이름의 마지막 3글자로 정렬 (중복되면 ID 기준)
SELECT Name FROM STUDENTS 
WHERE Marks > 75 
ORDER BY RIGHT(NAME, 3), ID ASC;

-- Employee Names   
SELECT NAME
FROM EMPLOYEE
ORDER BY NAME;