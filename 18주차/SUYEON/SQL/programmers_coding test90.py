# 겹치는 선분의 길이
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

def solution(lines):
    import collections
    return sum(1 for k, v in collections.Counter((i, i + 1) for x, y in lines for i in range(min(x, y), max(x, y))).items() if v > 1)
