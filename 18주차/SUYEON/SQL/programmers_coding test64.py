# 영어가 싫어요
def solution(numbers: str) -> int:
    return int(numbers.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("zero", "0"))

def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

# 문자열 계산하기
solution=eval

def solution(my_string: str) -> str:
    return eval(my_string)

def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

# 외계어 사전??
def solution(spell: list, dic: list):
    spell = {i: 0 for i in spell}

    for x in dic:
        if len(x) == len(spell):
            for y in x:
                if y in spell:
                    spell[y] += 1
                else:
                    break
            if len(set(spell.values())) == 1 and sum(set(spell.values())) == 1:
                return 1
            spell = {i: 0 for i in spell}

    return 2
