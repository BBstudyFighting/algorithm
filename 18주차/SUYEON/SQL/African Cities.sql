select city.name
from city
join COUNTRY on CITY.CountryCode = COUNTRY.Code
where COUNTRY.CONTINENT = 'Africa'