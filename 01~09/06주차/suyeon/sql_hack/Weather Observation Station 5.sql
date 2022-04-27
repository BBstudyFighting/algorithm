'''
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

STATION이라는 테이블에서, CITI name(Column명 CITY)이 가장 짧은 것과 긴 것을 출력하는 것입니다. 
이때 출력 시 주의할 점은, 같은 길이의 CITY name을 가진 것들에 대해서는 알파벳 순서가 가장 빠른 것을 출력하면 됩니다.

ASC: 오름차순
DESC: 내림차순
LENGTH: 문자열의 길이 조회 함수

'''
#짧은 길이
SELECT city, LENGTH(city) as length_char
FROM station
ORDER BY LENGTH(city) ASC, city ASC
LIMIT 1;
#긴 길이
SELECT city, LENGTH(city) as length_char
FROM station
ORDER BY LENGTH(city) DESC
LIMIT 1;
