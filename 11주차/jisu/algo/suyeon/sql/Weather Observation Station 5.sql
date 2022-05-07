'''
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

STATION이라는 테이블에서, CITI name(Column명 CITY)이 가장 짧은 것과 긴 것을 출력하는 것입니다. 
이때 출력 시 주의할 점은, 같은 길이의 CITY name을 가진 것들에 대해서는 알파벳 순서가 가장 빠른 것을 출력하면 됩니다.
'''

SELECT CITY, LENGTH(CITY) 
FROM STATION 
ORDER BY LENGTH(CITY), CITY LIMIT 1; 
SELECT CITY, LENGTH(CITY) 
FROM STATION 
ORDER BY LENGTH(CITY) DESC, CITY LIMIT 1;

##########
SELECT CITY, CHAR_LENGTH(CITY)
FROM STATION
ORDER BY 2 ASC,1 LIMIT 1;
SELECT CITY, CHAR_LENGTH(CITY)
FROM STATION
ORDER BY 2 DESC,1 DESC LIMIT 1;
#같은 길이를 가진 문자열이 여러 개 있을 수 있으므로, 알파벳 순으로 정렬하여 출력한다.


