'''
Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows:
표에 있는 총 city 항목 수와 고유 city 항목 수의 차이를 구하기
'''
select COUNT(city) - COUNT( DISTINCT city) # distinct CITY
from STATION 