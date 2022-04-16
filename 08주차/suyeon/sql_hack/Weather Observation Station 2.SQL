'''
The sum of all values in LAT_N rounded to a scale of  2decimal places.
The sum of all values in LONG_W rounded to a scale of  2decimal places.
'''
select round(SUM(LAT_N ),2), round(SUM(LONG_W ),2)
FROM STATION