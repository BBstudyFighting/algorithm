'''
Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. Round your answer to  4 decimal places.
스테이션에서 가장 작은 북위도(LAT_N)가 38.7780보다 큰 서부 경도(LONG_W)를 쿼리합니다. 당신의 답을 소수점 4자리까지 반올림하세요.
'''
select round(max(LONG_W),4)
from station
where LAT_N = (select min(LAT_N)
        from station
        where LAT_N >38.7780 )