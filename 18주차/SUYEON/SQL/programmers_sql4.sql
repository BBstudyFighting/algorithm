# 3월에 태어난 여성 회원 목록 출력하기
SELECT member_id, member_name, gender, date_format(date_of_birth, "%Y-%m-%d") as date_for_birth
from member_profile
where gender = 'W' and tlno is not null and date_format(date_of_birth, "%m") = "03";

select member_id, member_name, gender, date_format(date_of_birth, '%Y-%m-%d') as date_of_birth
from member_profile
where gender like 'w'
and tlno is not null
and month(date_of_birth) = 3;

