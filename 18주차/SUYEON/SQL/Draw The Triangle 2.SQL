set @NUMB = 0;
select repeat('* ', @NUMB := @NUMB + 1) 
from information_schema.tables 
LIMIT 20;