SELECT distinct CITY
FROM STATION 
WHERE not city regexp '^[a,e,i,o,u]'