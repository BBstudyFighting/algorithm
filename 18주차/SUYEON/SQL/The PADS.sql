-- 문제
-- 주어진 테이블의 Name을 알파벳 순서로 정렬해 출력하는데, 끝에 각 Name에 해당하는 Occupation의 첫 문자열을 첨가해서 출력시켜라. ex) James라는 이름이 Professor 직업을 갖고 있다면, James(P) 로 출력해라.
-- 각 Occpuation에 속하는 Name을 카운트해라. 이 때 다음과 같이 출력하는데, 1차 정렬기준은 [occupation_count] 오름차순으로 하고 2차 정렬기준은 [occpuation]의 알파벳 순서로 정렬해라.

SELECT CONCAT(name, '(', substring(occupation, 1, 1), ')')  # Substring : 문자열 일부 추출
FROM Occupations
ORDER BY name, substring(occupation, 1, 1);

SELECT CONCAT('There are a total of ', count(occupation), ' ', LOWER(occupation), 's.')
FROM Occupations
GROUP BY occupation
ORDER BY count(occupation), occupation

-- 첫번째 문제
-- occupation테이블의 모든 이름 목록을 알파벳 순서로 나열하고 각 직업의 첫 글자를 괄호 안에 묶어라
-- 이름과 직업의 첫글자를 select에 보여주기 위해 문자열을 합치는 concat을 사용
-- 정렬순서는 name과 occupation의 첫글자 순

-- 두번째 문제
-- occupation테이블에서 직업과 각 직업의 수를 오름차순으로 출력해라 직업은 소문자로 출력
-- 출력할 포맷은 'There are a total of [직업 수][직업명]s.'
-- occupation을 그룹으로 묶어서 count를 구해야하기 때문에 group by를 해줌
-- 순서는 occupation을 count로 묶어준 수, 두번째는 한 개 이상의 직업의 수가 같을 경우 알파벳순
-- 문자열은 concat으로 묶어서 출력하되 occupation이 소문자로 출력해야하므로 LOWER()함수 사용

# 오라클 버전
SELECT NAME || '(' || SUBSTR(OCCUPATION,1,1) || ')' FROM OCCUPATIONS
ORDER BY NAME;

SELECT 'There are a total of ' || COUNT(OCCUPATION) || ' ' || LOWER(OCCUPATION) || 's.' FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(OCCUPATION), OCCUPATION;
-- CONCAT 함수를 따로 쓸 필요없이 || 연산자로 한 열로 만들어주면 된다.