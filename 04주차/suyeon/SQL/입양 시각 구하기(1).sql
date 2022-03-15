SELECT HOUR(DATETIME) as 'HOUR', count(HOUR(DATETIME)) as 'COUNT' 
from ANIMAL_OUTS
# where HOUR(DATETIME) >= 9 and HOUR(DATETIME) < 20
where HOUR(DATETIME) between 9 and 20
group by HOUR
# Having Hour between 9 and 20
order by HOUR;
