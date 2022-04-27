'''
Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to  4decimal places.
STATION에서 137.2345보다 작은 가장 큰 북위도(LAT_N)에 대한 서부 경도(LONG_W)를 쿼리합니다. 당신의 답을 소수점 4자리까지 반올림하세요.
''''
select round(long_w, 4) #round : 반올림해주는 함수
from station
where lat_n = (select max(lat_n) 
     from station
     where lat_n < 137.2345)