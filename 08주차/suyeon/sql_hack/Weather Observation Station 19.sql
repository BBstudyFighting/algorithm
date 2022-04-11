'''
Consider  P1(a,c) and P2(b,d) to be two points on a 2D plane where (a,b) are the respective minimum and maximum values of Northern Latitude (LAT_N) and (c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the Euclidean Distance between points P1 and P2 and format your answer to display  4 decimal digits.

P1(a,c)과 P2(b,d)를 2D 평면의 두 점으로 간주하고, 여기서 (a,b)는 북위도(LAT_N)의 각 최소값과 최대값이고, (c,d)는 스테이션에서 서부 경도(LONG_W)의 각 최소값과 최대값이다.

점 P1과 P2 사이의 유클리드 거리를 쿼리하고 소수점 4자리를 표시하도록 답의 형식을 지정합니다.
'''
select round(SQRT(POW(MAX(LAT_N)-MIN(LAT_N),2) + POW(MAX(LONG_W)-MIN(LONG_W),2)),4)
FROM STATION
'''
p1(a,c), p2(b,d)
a, b = lat_n(위도)의 최소값, 최댓값 = min(lat_n), max(lat_n)
c, d = long_w(경도)의 최댓값, 최소값 = min(long_w), max(long_w)
유클리드 거리 = 피타고라스 정의 (a-b)^2 + (c-d)^2 
(P1.a - P1.b)^2+ (P2.a - P2.b)^2에서 루트 씌우기
먼저 각각 제곱한 값을 구하기 위해 POW() 함수 씌우기
그 수를 더한 값의 제곱근 구하기 위해 SQRT() 함수 씌우기
소수점 네번째 자리 수까지 반올림하기 위해 ROUND() 처리
''''