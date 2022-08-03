#자신의 봉급이 자신의 매니저보다 높은 사람들 모두 출력하는 것
SELECT E.Name as Employee
FROM Employee as E, Employee as M
WHERE E.ManagerId = M.Id AND E.Salary > M.Salary