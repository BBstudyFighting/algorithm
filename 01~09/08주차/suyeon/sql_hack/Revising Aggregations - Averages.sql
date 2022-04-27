'''
Query the average population of all cities in CITY where District is California.
district 값이 california 인 모든 도시의 평균 인구를 쿼리
'''
select avg(population) # avg: 평균
from CITY
where district = 'california'