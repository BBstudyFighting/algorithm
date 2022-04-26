'''
<복습>
Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
'''
SELECT name
from CITY
where population > 120000 and CountryCode = 'usa'