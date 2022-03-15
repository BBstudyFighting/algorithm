'''
처음에 SET을 이용하여 HOUR 변수에 -1을 넣어줌. 
그 다음, HOUR를 1씩 증가시키며 그에 따른 시간대별 입양 건수를 서브쿼리를 이용하여 만듦. 
HOUR는 0시부터 23시까지이므로 마지막에 WHERE로 23시까지의 조건을 넣어주고 풀었음.

SQL의 경우, 다른 프로그래밍 언어와 다르게 SET을 이용할 때는 대입 연산자를 '='를 사용하고 그 외에는 :=를 사용해야 함. 
보통 SQL에서는 '='를 비교 연산자로 사용하므로 꼭 ':='를 사용해야 함.
'''

SET @HOUR = -1;
SELECT (@HOUR := @HOUR +1) AS HOUR,
(SELECT COUNT(HOUR(DATETIME)) 
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME)=@HOUR) AS COUNT 
FROM ANIMAL_OUTS
WHERE @HOUR < 23;

'''
변수 생성) SET @[변수이름] := 값;
리네이밍) AS '[리네이밍할 이름]'

'''
