-- [문제출처 HACKER RANK](https://www.hackerrank.com/domains/sql)
-- 문제의 저작권은 해커랭크에 있습니다

-- ### 문제소개
-- ```sql
-- - 직업별로 4개의 컬럼을 구성한다 (의사, 교수, 가수, 배우)
-- - 1행에 알파벳이 가장 빠른 이름이 오며, 나머지 이름도 알파벳순 정렬 
-- - 직업별 인원이 가장 많은 컬럼을 기준으로 하고, 
--   그 인원에 미치지 못하는 컬럼의 행은 NULL 로 표시
-- ```
-- ### 풀이접근
-- ```sql
-- - 테이블 피벗팅(행 → 열) 필요
-- - 가장 사람이 많은 컬럼 기준 잡기 : MAX 
-- - 기준보다 적은 컬럼의 행 NULL 로 표시 : GROUP BY
-- - ROW_NUMBER, 조건 집합 : 행번호를 조건이 적용된 집합에 적용함 
-- ```

-- ### 코드
-- ```sql
SELECT -- 직업별 인원수 구하기
	MAX(CASE WHEN OCCUPATION = 'DOCTOR' THEN NAME END) 'DOCTOR',
	MAX(CASE WHEN OCCUPATION = 'PROFESSOR' THEN NAME END) 'PROFESSOR',
	MAX(CASE WHEN OCCUPATION = 'SINGER' THEN NAME END) 'SINGER'.
	MAX(CASE WHEN OCCUPATION = 'ACTOR' THEN NAME END) 'ACTOR'
FROM ( -- NAME 순서로 정렬된 OCCUPATION 에 행번호를 매김
	SELECT *, ROW_NUMBER() OVER (PARTITION BY OCCUPATION ORDER BY NAME) RN
    FROM OCCUPATIONS ) T  -- 그리고 그것을 피벗 
GROUP BY RN -- 위에서 정의한 RN 으로 그룹화해서 조회
-- ```

