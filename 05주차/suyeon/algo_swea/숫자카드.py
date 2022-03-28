'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''
length = int(input())
for l in range(1, length+1):
    size = input()
    temp = list(map(int, list(input())))
    #각 자리수를 카운팅하기 위해 사용
    numcheck = [0]*10
    #각 자리수 카운팅하기
    for t in temp:  numcheck[t] += 1
    #숫자와 횟수를 적기위한 변수
    index = maxnum = 0
    #반복문을 돌면서 찾는다
    for i in range(9, -1, -1):
        if numcheck[i] > maxnum :
            maxnum = numcheck[i]
            index = i
    #출력
    print("#{} {} {}".format(l, index, maxnum))
