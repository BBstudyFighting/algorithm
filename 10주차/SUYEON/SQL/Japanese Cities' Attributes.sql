'''
Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
'''
SELECT *
from CITY
where COUNTRYCODE = 'JPN'