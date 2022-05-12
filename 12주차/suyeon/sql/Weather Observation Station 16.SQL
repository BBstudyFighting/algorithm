'''
Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780. Round your answer to 4 decimal places.
'''
select Round(LAT_N, 4)
from STATION 
where LAT_N >38.7780
order BY LAT_N limit 1