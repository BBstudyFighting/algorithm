# 진료과별 총 예약 횟수 출력하기
SELECT MCDP_CD AS 진료과코드, COUNT(APNT_YMD) AS 5월예약건수
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY 2,1 
# 같은 뜻 ORDER BY 5월예약건수	, 진료과코드
# 숫자가 조회되었을 때의 컬럼 순서

SELECT MCDP_CD as '진료과코드' , count(APNT_YMD) as '5월예약건수'
from APPOINTMENT  
where date_format(APNT_YMD , '%Y-%m') = '2022-05'
group by MCDP_CD
order by 5월예약건수 , 진료과코드