#IFNULL 사용하기
SELECT ANIMAL_TYPE, IFNULL(NAME,'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

#case 사용하기
select ANIMAL_TYPE,
    case 
    when NAME is null then 'No name' 
    else NAME end 
    as NAME,
    SEX_UPON_INTAKE
from ANIMAL_INS
order by ANIMAL_ID;