def solution(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums))  # 로또 맞힌 숫자 갯수
    cnt_0 = lottos.count(0)  # 로또에서 낙서로 지워진 부분

    # 0을 다 맞다고 봤을 때와 아닐때 값 구하기
    return [7-max(cnt+zero, 1), 7-max(cnt, 1)]
