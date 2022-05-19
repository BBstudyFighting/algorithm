'''
Query the average population for all cities in CITY, rounded down to the nearest integer.
가장 가까운 정수로 내림한 CITY의 모든 도시에 대한 평균 인구를 쿼리합니다.
'''
SELECT round(avg(population)) *round:반올림 함수
FROM CITY
