'''
Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.

 a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4decimal places.

P1(a,b)과 P2(c,d)를 2D 평면의 두 점이라고 가정하자.
a는 북위도의 최소값과 같습니다(STATION의 LAT_N).
b는 서부 경도의 최소값과 같습니다(STATION의 LONG_W).
c는 북위도의 최대값과 같습니다(STATION의 LAT_N).
d는 서부 경도의 최대값과 같습니다(STATION의 LONG_W).
점 사이의 맨하탄 거리를 쿼리하고 소수점 4자리 척도로 반올림합니다
'''
select round((max(LAT_N)-min(LAT_N)) + (max(LONG_W)-min(LONG_W)) ,4)
from STATION ;

select round(abs(max(LAT_N)-min(LAT_N)) + abs(max(LONG_W)-min(LONG_W)) ,4) #abs: 절댓값을 구하는 함수
from STATION ;
