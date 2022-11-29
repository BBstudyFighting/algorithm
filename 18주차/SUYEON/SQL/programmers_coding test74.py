# 진료순서 정하기
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]


def solution(emergency):
    e = sorted(emergency,reverse=True)
    return [e.index(i)+1 for i in emergency]


