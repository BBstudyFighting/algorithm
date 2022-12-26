# 흉부외과 또는 일반외과 의사 목록 출력하기
select dr_name, dr_id, mcdp_cd, date_format(hire_ymd,'%Y-%m-%d')
from doctor
where mcdp_cd = 'CS' or mcdp_cd = 'GS'
order by hire_ymd desc, dr_name asc;

SELECT DR_NAME, DR_ID, MCDP_CD, LEFT(HIRE_YMD,10) #HIRE_YMD을 왼쪽부터 10글자 출력
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC