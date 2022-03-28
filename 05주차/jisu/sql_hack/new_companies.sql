-- 회사코드, 설립자 이름, 직급별 직원수(count)
select c.company_code, c.founder,  
	count(distinct(e.lead_manager_code)),
    count(distinct(e.senior_manager_code)),
    count(distinct(e.manager_code)),
    count(distinct(e.employee_code))
from employee e join company c on e.company_code = c.company_code
group by c.company_code, c.founder
order by 1; -- 첫번째 컬럼을 기준으로 정렬