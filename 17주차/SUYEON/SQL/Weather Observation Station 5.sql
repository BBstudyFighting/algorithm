select CITY, LENGTH(CITY)
from STATION
order by LENGTH(CITY), CITY LIMIT 1;
select CITY, LENGTH(CITY)
from STATION
order by LENGTH(CITY) DESC, CITY LIMIT 1;
# 세미클론 무조건 붙여주기!! 안 그럼 런타임 오류 발생