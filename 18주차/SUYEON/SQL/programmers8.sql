#1 보호소에서 중성화한 동물
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE,I.NAME FROM ANIMAL_INS AS I 
LEFT JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID  = O.ANIMAL_ID 
WHERE I.SEX_UPON_INTAKE != O.SEX_UPON_OUTCOME
ORDER BY I.ANIMAL_ID

select animal_id, animal_type, name 
from animal_ins
where sex_upon_intake like 'intact%' and animal_id in (select animal_id from animal_outs where sex_upon_outcome like 'spayed%' or sex_upon_outcome like 'neutered%')

#2 루시와 엘라 찾기
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')

#3 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE = 'DOG'
ORDER BY NAME