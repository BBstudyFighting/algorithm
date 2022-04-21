"""
Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use 'NULL' as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

Write a query to help Eve.
등급 순, 이름 순으로 학생들의 이름, 등급, 점수를 조회하는 조인 문제
등급이 8미만인 학생의 이름은 null 처리 조건
"""
SELECT IF(G.GRADE >= 8, S.NAME, 'NULL'), G.Grade, S.Marks # 등급이 8미만인 학생의 이름은 null 처리
FROM STUDENTS AS S 
INNER JOIN GRADES AS G 
ON S.MARKS BETWEEN G.MIN_MARK AND G.MAX_MARK # BETWEEN A AND B : 조건 A 에서 조건 B 사이의 값을 조회
ORDER BY G.GRADE DESC, S.NAME, S.MARKS ASC ;

# their name and list them by their grades in descending order
# their marks in ascending order 

Select case when g.grade >= 8 then s.name
else NULL end, g.grade, s.marks
from STUDENTS as S
join grades as g on (s.marks >= g.MIN_MARK AND s.marks <=  g.MAX_MARK)
ORDER BY G.GRADE DESC, S.NAME, S.MARKS ASC ;