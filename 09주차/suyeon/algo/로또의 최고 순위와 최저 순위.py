def solution(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums)) 
    #set :  집합의 성질을 가지고 있는 함수, 중복되지 않은 원소를 얻고자 할 때 사용
    zero = lottos.count(0)
    
    return [7-max(cnt+zero,1) ,7-max(cnt,1)]



def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1] # 1개나 2개가 정답일때는 어차피 6등이라 rank을 저렇게 지정

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]