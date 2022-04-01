'''
Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
'''
select * from city
where COUNTRYCODE = 'JPN' # 여기서 따옴표 까먹지 말기
