'''
Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
'''
select DISTINCT CITY
from STATION
where id%2 =0 # 짝수 ID number