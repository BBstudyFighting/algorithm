'''
Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to  4 decimal places.
'''
select Truncate(max(LAT_N),4) #Truncate: 소수점
from STATION
where LAT_N < 137.2345 ; 