SELECT ANIMAL_ID, name, DATETIME
from ANIMAL_INS
order by name asc, datetime desc 
# 단 이름이 같은 동물 중에서는 보호를 먼저 시작한 동물을 먼저 보여달라고 하니
# name으로 한번 오름차순 정렬하고 그 다음에 datetime으로 내림차순 정렬을 해야 된다는 말이다
