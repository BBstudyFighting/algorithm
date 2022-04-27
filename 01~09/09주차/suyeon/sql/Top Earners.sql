"""
We define an employee's total earnings to be their monthly salary X months worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as 2 space-separated integers.

직원의 총 수입은 월별 근로로 정의되며, 최대 총 수입은 직원 테이블에 있는 모든 직원의 최대 총 수입으로 정의됩니다. 전체 직원의 최대 총 수입과 최대 총 수입이 있는 직원 수를 찾기 위해 쿼리를 작성하십시오. 그런 다음 이 값을 공백으로 구분된 정수로 인쇄합니다.
"""
select salary*months as earnings, count(*)
from employee
group by earnings
order by earnings desc limit 1

'''
total earnings은 salary * months로 정의
total earnings를 계산해놓고 그 중에서 제일 많이 번 사람을 maximum total earnings로 정의
MAX(salary*months)로 했다가 오류가 남 > 저 상태에서 max는 불가능! 
그래서 가장 잘 버는 사람이 몇 명인지 구하기 > LIMIT 1
'''

SELECT salary * months as earnings, count(*)
FROM Employee
WHERE salary * months = (SELECT max(salary * months) From Employee)
GROUP BY earnings

########

SELECT months * salary as earnings, count(*)
FROM Employee
GROUP BY earnings
HAVING earnings = (SELECT max(months*salary) FROM employee)