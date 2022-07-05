select round(abs(max(lat_n) - min(lat_n)) + abs(max(long_w) - min(long_w)) , 4) 
from station
#abs : 절댓값 구하는 함수, 없어도 실행되기는 함