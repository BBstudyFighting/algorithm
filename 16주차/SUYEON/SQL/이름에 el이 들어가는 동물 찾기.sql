SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE = 'DOG' 
ORDER BY NAME
# LIKE : 특정 부분이 일치하는 데이터를 찾고싶을때,  _ 혹은 %를 이용(_:_ 개수만큼 데이터가 있다는 뜻, % :%는 글자수와 상관없이 찾는다는 뜻)