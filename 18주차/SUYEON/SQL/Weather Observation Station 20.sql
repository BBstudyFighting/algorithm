-- STATION 테이블에서 LAT_N 컬럼의 중앙값을 쿼리해라. 그리고 해당 값을 소수점 4자리까지 반올림하여 나타내라.
SELECT ROUND(LAT_N,4)
FROM (SELECT LAT_N, PERCENT_RANK() OVER (ORDER BY LAT_N ASC) percent
      FROM STATION) A
WHERE percent=0.5;
-- PERCENT_RANK 함수는 해당 그룹 내의 백분위 순위(Percentil Rank)를 반환한다. 0초과 1이하의 누적분포 값을 반환하는 CUME_DIST와는 달리, PERCENT_RANK는 0이상 1이하의 값을 반환한다.
-- 백분위 순위란 개념 자체가 그룹 안에서 해당 로우의 값보다 작은 값의 비율이므로 그 값이 0.5인 값을 구해주면 중앙값이 된다.

SELECT ROUND(LAT_N,4)
FROM STATION AS S
WHERE (SELECT COUNT(*) FROM STATION WHERE LAT_N < S.LAT_N) = (SELECT COUNT(*) FROM STATION WHERE LAT_N > S.LAT_N)