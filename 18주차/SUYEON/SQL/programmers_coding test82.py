# 치킨 쿠폰
def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer

def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        answer += chicken
        chicken += mod
    return answer

# 옹알이(1)
from itertools import permutations
def solution(babbling):
    answer = 0
    speek = ["aya","ye","woo","ma"]
    word = []
    for i in range(1, len(speek)+1):
        for j in permutations(speek, i):
            word.append(''.join(j))

    for i in babbling:
        if i in word:
            answer += 1
    return answer


def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c