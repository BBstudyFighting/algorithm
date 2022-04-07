'''
Query the Name of any student in STUDENTS who scored higher than 75Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
marks가 75보다 높은 학생들을 쿼리. 이름의 마지막 3글자로 정렬하고 중복된다면 오름차순 id로 정렬
'''
SELECT name
from students
where marks > 75
Order by right(name,3), id ASC;

#right: 문자열의 오른쪽 기준으로 n개의 문자를 가져오는 함수