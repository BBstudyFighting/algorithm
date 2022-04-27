'''
Query the total population of all cities in CITY where District is California.
district 값이 california 인 모든 도시의 총 인구 조회
'''
select sum(population)
from CITY
where District = 'California'