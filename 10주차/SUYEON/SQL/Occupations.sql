'''
각각의 이름을 알파벳순으로 정렬하고 그에 상응하는 직업(Occupation)을 보여주는데, 직업값을 기준으로 Pivot 테이블로 변환해라. 이 때 변환한 Pivot 테이블의 칼럼명은 Doctor, Professor, Singer, Actor 순이다. 참고로, 각 직업에 대응하는 이름이 없다면 NULL을 반환해라
'''
# 1번째 방법
SELECT
    MAX(CASE WHEN OCCUPATION = 'Doctor' THEN NAME END) AS 'Doctor',
    MAX(CASE WHEN OCCUPATION = 'Professor' THEN NAME END) AS 'Professor',
    MAX(CASE WHEN OCCUPATION = 'Singer' THEN NAME END) AS 'Singer',
    MAX(CASE WHEN OCCUPATION = 'Actor' THEN NAME END) AS 'Actor'
FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY OCCUPATION ORDER BY NAME) RN
      FROM OCCUPATIONS) TEMP
GROUP BY RN

-- OVER (PARTITION BY ...): 그룹 단위로 나누어 무언가를 해보겠다는 뜻, 위 코드에서는 row_number 를 name 순서대로 정렬된 occupation 별로 숫자를 매기겠다는 뜻이다.
-- 바로 '집계함수'가 존재해야 GROUP BY 를 사용할 수 있기 때문/ 값이 존재하지 않는다면 NULL 값으로 처리해주기 위해 쓸모없는 MAX 를 넣어준 것이다. (STRING 이라서 MAX가 들어간다고 딱히 출력값이 변하지 않는다.
-- 마지막에 GROUP BY RN 을 써주었는데, 이는 바로 RN이 1인 것끼리 맨 윗줄에 출력하고, 2인것 끼리 두번쨰줄에 출력하고,,, 를 수행하기 위해 Group by 를 취해준 것이다.

# 2번째 방법
-- 각 직업별 Index를 세기 위한 변수 설정
SET @D=0, @P=0, @S=0, @A=0;

-- 문자열의 알파벳순서에서 최솟값(MIN)은 A(a)로 시작하는 것을 추출해줌!
SELECT MIN(Doctor), MIN(Professor), MIN(Singer), MIN(Actor)
FROM (SELECT CASE WHEN Occupation = 'Doctor' THEN Name END AS Doctor,
             CASE WHEN Occupation = 'Professor' THEN Name END AS Professor,
             CASE WHEN Occupation = 'Singer' THEN Name END AS Singer,
             CASE WHEN Occupation = 'Actor' THEN Name END AS Actor,
             CASE
             WHEN Occupation = 'Doctor' THEN (@D:=@D+1)
             WHEN Occupation = 'Professor' THEN (@P:=@P+1)
             WHEN Occupation = 'Singer' THEN (@S:=@S+1)
             WHEN Occupation = 'Actor' THEN (@A:=@A+1)
             END AS RowNumber
       FROM Occupations
       ORDER BY Name) sub
GROUP BY RowNumber

-- (Name을 알파벳순으로 정렬했을 때)각 직업별로 첫 번째로 오는 Name들, 두 번째로 오는 Name들, 세 번째로 오는 Name들...(생략)을 알아내기 위해 SET 을 이용해 각 직업별의 Row를 세어준다.
-- CASE WHEN을 사용해 Row의 값을 Column으로 Pivot table을 만들어주기