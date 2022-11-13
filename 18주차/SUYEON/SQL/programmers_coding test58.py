# 문자열 정렬하기 (2)
def solution(my_string):
    return ''.join(sorted(my_string.lower()))

# 피자 나눠 먹기 (2)
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1
        
def solution(n):
    answer = 1
    while 6 * answer % n:
        answer += 1
    return answer

# 369게임
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

def solution(order: int) -> int:
    return sum([1 for x in str(order) if x in ['3', '6', '9']])

if __name__ == '__main__':
    print(solution(3))      # 1
    print(solution(29423))  # 2
    
# 모스부호 (1)
def solution(letter):
    morse = {
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }

    return ''.join([morse[i] for i in letter.split(' ')])