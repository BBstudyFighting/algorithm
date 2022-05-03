def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:  # 참인 경우 더하기
            answer += absolutes[i]
        else:  # 거짓인 경우 뺴기
            answer -= absolutes[i]
    return answer
