'''
Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows:
표에 있는 총 city 항목 수와 고유 city 항목 수의 차이를 구하기
'''
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) #COUNT: 행 개수 구하기
FROM STATION
