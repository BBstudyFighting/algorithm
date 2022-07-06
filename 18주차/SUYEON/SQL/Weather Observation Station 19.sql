select round(SQRT(POW(MAX(LAT_N)-MIN(LAT_N),2) + POW(MAX(LONG_W)-MIN(LONG_W),2)),4)
FROM STATION

-- 각각 제곱한 값을 구하기 위해 POW() 함수 씌우기
-- 그 수를 더한 값의 제곱근 구하기 위해 SQRT() 함수 씌우기
-- 소수점 네번째 자리 수까지 반올림하기 위해 ROUND() 처리