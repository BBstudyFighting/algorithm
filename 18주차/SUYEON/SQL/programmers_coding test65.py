# 등수 매기기
def solution(score: list) -> list:
    dict, avg_list = {}, [sum(num) / 2 for num in score]

    for index, avg in enumerate(sorted(avg_list, reverse=True), start=1):
        if avg not in dict:
            dict[avg] = index

    return [dict[avg] for avg in avg_list]

def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]
