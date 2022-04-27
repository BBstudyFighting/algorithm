'''
Query the sum of Northern Latitudes (LAT_N) from STATION having values greater 38.7880 than  and less than 137.2345. Truncate your answer to  4 decimal places.
38.7880보다 크고 137.2345보다 작은 LAT_N의 합을 구하고 4번째에서 내림하라
'''
select Truncate(sum(LAT_N),4) #Truncate: 소수점
from STATION
where LAT_N > 38.7880 and LAT_N < 137.2345 ; 