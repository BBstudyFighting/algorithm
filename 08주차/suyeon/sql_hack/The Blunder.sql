"""
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's 0 key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary. 

Write a query calculating the amount of error (i.e.: actual - miscalculated average monthly salaries), and round it up to the next integer.

사만다는 직원 테이블에 있는 모든 직원의 평균 월급을 계산하는 일을 맡았지만 계산을 마친 후에야 키보드의 0 키가 고장 났다는 것을 알았다. 그녀는 자신의 오산(0을 빼고 계산)과 실제 평균 급여 간의 차이를 찾는 데 도움을 받고자 합니다.

오류의 양(즉, 실제 평균 급여 - 잘못 계산된 월평균 급여)을 계산하는 질의를 작성하여 다음 정수로 반올림합니다.
"""
select ceil(avg(salary)-avg(replace(salary,0,''))) 
#ceil:  올림, replace('문자열','기존의 변경될 문자열','변경할 문자열')
from EMPLOYEES 