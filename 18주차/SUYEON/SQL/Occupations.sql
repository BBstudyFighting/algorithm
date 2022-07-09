-- 각각의 이름을 알파벳순으로 정렬하고 그에 상응하는 직업(Occupation)을 보여주는데, 직업값을 기준으로 Pivot 테이블로 변환해라. 이 때 변환한 Pivot 테이블의 칼럼명은 Doctor, Professor, Singer, Actor 순이다. 참고로, 각 직업에 대응하는 이름이 없다면 NULL을 반환해라
SELECT
    MAX(CASE WHEN OCCUPATION = 'Doctor' THEN NAME END) AS 'Doctor',
    MAX(CASE WHEN OCCUPATION = 'Professor' THEN NAME END) AS 'Professor',
    MAX(CASE WHEN OCCUPATION = 'Singer' THEN NAME END) AS 'Singer',
    MAX(CASE WHEN OCCUPATION = 'Actor' THEN NAME END) AS 'Actor'
FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY OCCUPATION ORDER BY NAME) RN
      FROM OCCUPATIONS) TEMP
GROUP BY RN

-- RANK
-- 공동 순위만큼 건너뜀 (ex: 1,2,2,4 ...)
-- DENSE_RANK
-- 공동 순위를 뛰어넘지 않음 (ex: 1,2,2,3 ...)
-- ROW_NUMBER
-- 공동 순위를 무시함 (ex: 1,2,3,4 ...)
SELECT MIN(CASE WHEN Occupation LIKE 'D%' THEN Name END)AS Docter
     , MIN(CASE WHEN Occupation LIKE 'P%' THEN Name END)AS Professor
     , MIN(CASE WHEN Occupation LIKE 'S%' THEN Name END)AS Singer
     , MIN(CASE WHEN Occupation LIKE 'A%' THEN Name END)AS Actor
FROM (
SELECT a.Occupation as Occupation,
         a.Name as Name,
         (SELECT COUNT(*) 
            FROM Occupations AS b
            WHERE a.Occupation = b.Occupation AND a.Name > b.Name) as Rank_num
FROM Occupations AS a
ORDER BY a.Occupation, a.Name ) as tmp
GROUP BY tmp.Rank_num

SELECT 
    MIN(CASE WHEN OCCUPATION = 'DOCTOR' THEN NAME ELSE NULL END) ,
    MIN(CASE WHEN OCCUPATION = 'PROFESSOR' THEN NAME ELSE NULL END) ,
    MIN(CASE WHEN OCCUPATION = 'SINGER' THEN NAME ELSE NULL END) ,
    MIN(CASE WHEN OCCUPATION = 'ACTOR' THEN NAME ELSE NULL END)
FROM (SELECT OCCUPATION, NAME, ROW_NUMBER() OVER (PARTITION BY OCCUPATION ORDER BY NAME) rn FROM OCCUPATIONS) as tmp
GROUP BY tmp.rn