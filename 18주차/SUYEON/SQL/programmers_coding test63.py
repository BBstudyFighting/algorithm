# 한 번만 등장한 문자
def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer

# 잘라서 배열로 저장하기
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]