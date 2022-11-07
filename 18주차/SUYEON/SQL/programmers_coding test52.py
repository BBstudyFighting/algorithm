# 아이스 아메리카노
def solution(money):
    answer = [money // 5500, money % 5500]
    return answer

# 문자열 뒤집기
def solution(my_string):
    return my_string[::-1]

def solution(my_string: str) -> str:
    return my_string[::-1]  # 역슬라이싱

if __name__ == '__main__':
    print(solution("jaron"))  # "noraj"
    print(solution("bread"))  # "daerb"


# 배열 원소의 길이
def solution(strlist: list) -> list:
    return [len(x) for x in strlist]

if __name__ == '__main__':
    print(solution(["We", "are", "the", "world!"]))  # [2, 3, 3, 6]
    print(solution(["I", "Love", "Programmers."]))   # [1, 4, 12]


def solution(strlist):
    answer =[]
    for i in strlist:
        answer.append(len(i))
    return answer

# 배열 자르기
def solution(numbers: list, num1: int, num2: int) -> list:
    return numbers[num1:num2+1]

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5], 1, 3))  # [2, 3, 4]
    print(solution([1, 3, 5], 1, 2))  # [3, 5]
    
    
def solution(numbers, num1, num2):
    answer = []
    return numbers[num1:num2+1]