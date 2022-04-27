"""
P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* * * * * 
* * * * 
* * * 
* * 
*
Write a query to print the pattern P(20).
"""
SET @number = 21; 
# SET @변수이름 = 변수의 값
# 20이 아니라 21로 한것은 " @variable := @variable -1 " 이런식으로 -1을 대입해주면서 점점 갯수를 줄여나갈것이기 때문이다.
SELECT REPEAT('* ', @number := @number - 1) 
# =뒤의 내용을 부여하는것이고 :=는 대입해준다고 보면된다.
FROM information_schema.tables; 
#information_schema: MySQL 서버 내에 존재하는 DB의 메타 정보(테이블, 칼럼, 인덱스 등의 스키마 정보)를 모아둔 DB
#TABLES: 생성된 모든 테이블 정보