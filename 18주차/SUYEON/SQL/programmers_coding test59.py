# 인덱스 바꾸기
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)

# 외계행성의 나이
def solution(age):
    return ''.join([chr(int(i)+97) for i in str(age)])

# 배열 회전시키기
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]


from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

# 암호 해독
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer