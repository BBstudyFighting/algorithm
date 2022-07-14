-- STATION이라는 테이블에서, CITI name(Column명 CITY)이 가장 짧은 것과 긴 것을 출력하는 것입니다. 
-- 이때 출력 시 주의할 점은, 같은 길이의 CITY name을 가진 것들에 대해서는 알파벳 순서가 가장 빠른 것을 출력하면 됩니다.
select city, LENGTH(city)
from station 
order by LENGTH(city), city LIMIT 1;

select city, LENGTH(city)
from station 
order by LENGTH(city) DESC, city LIMIT 1;