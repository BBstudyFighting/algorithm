SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, "%Y-%M-%M") #DATE_FORMAT(값, '원하는 형태')
FROM ANIMAL_INS
WHERE ANIMAL_ID

# 자주쓰는 date 형식
-- %Y : 4자리 연도
-- %y : 2자리 연도
-- %m : 2자리 월
-- %d : 2자리 일
-- %H : 24시간 형식 시(00-23)
-- %h : 12시간 형식 시(01-12)
-- %i : 2자리 분(0-59)
-- %S, %s : 2자리 초(0-59)