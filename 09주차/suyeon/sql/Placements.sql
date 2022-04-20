"""
You are given three tables: Students, Friends and Packages. Students contains two columns: ID and Name. Friends contains two columns: ID and Friend_ID (ID of the ONLY best friend). Packages contains two columns: ID and Salary (offered salary in $ thousands per month).

Write a query to output the names of those students whose best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.

(자신의 친구(베스트 프렌드)가 자신보다 더 높은 Salary를 받은 학생들(자신들)의 이름을 출력해라. 이 때 자신의 베스트 프렌드가 받는 Salary를 오름차순 기준으로 정렬해라. 단, 동일한 값으로 Salary가 제공된 적은 없다.(중복된 값은 없다는 의미)
"""
Select S.NAME
FROM STUDENTS S 
JOIN FRIENDS F ON S.ID = F.ID
JOIN PACKAGES P1 ON S.ID = P1.ID
JOIN PACKAGES P2 ON F.FRIEND_ID = P2.ID
WHERE P2.SALARY > P1.SALARY
ORDER BY P2.SALARY;
"""
세 개의 테이블을 모두 사용해야 값을 추출할 수 있기 때문에, 세 개 테이블을 모두 조인해준다.
조인을 세 번 하면 아래와 같이 총 8개의 column 을 갖는 테이블이 완성된다.

이 조인 테이블에서 값, 즉 나의 salary(p1.Salary) 보다 친구의 salary(p2.Salary) 가 더 높은 것을 where 에 조건문으로 달아서 필터링하면 된다. 
"""