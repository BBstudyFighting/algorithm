# 위장
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2 
            #첨에 딕셔너리에 해당 종류의 의상이 없을 때 그 의상을 더 해주면서 아무것도 안입었을때의 경우를 함께 생각해서 2를 더해줍
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num # cnt x num

    return cnt - 1