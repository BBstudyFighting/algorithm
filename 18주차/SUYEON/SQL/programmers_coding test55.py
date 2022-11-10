# 자릿수 더하기
def solution(n):
    return sum(list(map(int, str(n))))

# 배열 뒤집기
def solution(num_list):
    answer = []
    answer = num_list[::-1]
    return answer

# 모음 제거
def solution(my_string):
    collection = ("a, e, i, o, u")
    for i in collection :
        my_string = my_string.replace(i,"")
    return my_string

def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string

# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = 0
    for c in my_string:
        if c.isnumeric():
            answer += int(c)
    return answer

def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())