'''
<복습>
Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
'''
SELECT *
from city
where population > 100000 and CountryCode = 'usa' ;

# 조건) populations larger than 100000 / CountryCode for America is USA

