T = int(input())
for tc in range(1, T + 1):
    str1 = input() #문자열이라서 그냥받음
    str2 = input()

    N = len(str1)
    M = len(str2)
    str2subsetN =[] #N개의 문자열을가진 str2의 부분집합문자열
    str2 = zzzzzabczzzzzz
    for i in range(M-N+1): 
        #M-N개째에서부터 N개의 문자열을 구하면 전체가끝이나므로 끝숫자는 미만을 뜻하므로 1을 더해줌
        str2subsetN.append(str2[i:i+N]) #문자열슬라이싱으로 구함
    
    if not str2subsetN.count(str1) ==0: 
        #부분집합에 str1과 같은값이있으면 1출력
        answer = 1
    else:
        answer = 0
    print(f'#{tc} {answer}')
