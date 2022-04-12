'''
A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.
STATION 테이블에서 LAT_N 컬럼의 중앙값을 쿼리해라. 그리고 해당 값을 소수점 4자리까지 반올림하여 나타내라.
'''
# 실패한 코드 : 찾아보니 오라클에서는 적용된다고 함
select round(median(LAT_N),4)
from STATION ;

#성공한 코드
SET @rowIndex=-1; 
#SET을 활용해 테이블 행의 숫자를 세주기, -1이라고 설정하는 이유는 이후에 중앙값을 찾을 때 데이터 개수가 홀수/짝수에 따라 설정 방법이 달라지기 때문
SELECT ROUND(AVG(lat_n), 4) AS Median
FROM (SELECT @rowIndex:=@rowIndex+1 AS RowNumber,
                lat_n
      FROM station
      ORDER BY lat_n) sub
WHERE RowNumber IN (FLOOR(@rowIndex / 2), CEIL(@rowIndex / 2)) 
# 0: 100, 1: 200, 2: 300, 3: 400, 4 :500
# 짝수일 때 FLOOR(내림 처리)하면 1, CEIL(올림 처리)하면 2가 되게 된다,따라서 올림, 내림처리한 각각의 RowNumber에 해당하는 Value 2개를 평균값을 내게 되면 중앙값이 된다.
# 홀수일 때 마지막 RowNumber인 4를 2로 나누게 되면 2로 나누어떨어진다.
# 데이터 개수에 상관없이 첫 데이터 행의 Index가 0으로 시작할 때, 마지막 행 Index를 가지고 중앙값을 계산해낼 수 있다
#마지막으로 주의해야 할 점은 WHERE 구문에 마지막 행 Index를 정의해줄 때 RowNumber이 아닌 @rowIndex인 이유는 서브쿼리 구문에서 @rowIndex := @rowIndex+1 로 계속적으로 더해주었고 결국 마지막에 최종적으로 할당된 @rowIndex 변수에는 마지막 행의 Index가 담겨있기 때문이다
####https://techblog-history-younghunjo1.tistory.com/160####