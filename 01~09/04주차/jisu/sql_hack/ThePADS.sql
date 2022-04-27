-- [문제출처 HACKER RANK](https://www.hackerrank.com/domains/sql)
-- 문제의 저작권은 해커랭크에 있습니다

-- ### 문제소개
-- ```sql
-- 1. 이름 뒤에 직업스펠링의 첫글자를 표시 
-- 	Name:Ashely + Occupation:Professor = Ashely(P)
-- 2. 직업별로 몇 명이 있는지 출력
-- 	There are a total of 2 doctors.
-- ```
-- ### 풀이접근
-- ```sql
-- - 1번 : LEFT 활용해서 OCCUPATION의 첫 글자를 가져옴
-- - 2번 : CONCAT, COUNT 활용
-- ```

-- ### 코드
-- ```sql
-- 1번 쿼리
SELECT CONCAT(NAME,'(',LEFT(OCCUPATION,1),')')
FROM OCCUPATIONS ORDER BY NAME;

-- 2번 쿼리
SELECT
    CONCAT('There are a total of ',COUNT(OCCUPATION),
           ' ',LOWER(OCCUPATION),'s.')
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(OCCUPATION), OCCUPATION
-- ```