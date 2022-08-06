SELECT d.name AS department
      ,e.name AS Employee
      ,e.salary AS salary
FROM Employee AS e
    INNER JOIN ( SELECT departmentid, MAX(salary) AS max_salary   
    -- departmendID 별로 top salary 데이터 구함
            FROM employee
            GROUP BY departmentid
            ) AS dh ON e.departmentid = dh.departmentid
                   AND e.salary = dh.max_salary
    INNER JOIN department AS d ON d.id = e.departmentid

select D.name Department,E.name Employee,E.salary Salary
from Department D join (
    select E1.departmentId,E1.name,E2.salary
    from Employee E1,(
        select departmentId,max(salary) salary
        from Employee
        group by departmentId
    )E2
    where E1.salary=E2.salary and E1.departmentId=E2.departmentId
)E on D.id=E.departmentId;