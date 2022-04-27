'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''
# 카운팅문제는 각 번호의 개수를 저장할 리스트를 만든후에 나온 카드의 번호에 해당하는 인덱스에 접근하여 갯수를 하나씩 늘린뒤에 뒤부터 검사하여 제일 많이나온 카드를 확인
# 같은 장수라면 패쓰하는 형식으로 하여 제일 큰 값인 카드를 출력

length = int(input())
for l in range(1, length+1):
    size = input()
    temp = list(map(int, list(input()))  #각 자리수를 카운팅하기 위해 사용
    numcheck = [0]*10 #각 자리수 카운팅하기
    for t in temp:  numcheck[t] += 1 #숫자와 횟수를 적기위한 변수
    index = maxnum = 0 #반복문을 돌면서 찾는다
    for i in range(9, -1, -1):
        if numcheck[i] > maxnum :
            maxnum = numcheck[i]
            index = i
    #출력
    print("#{} {} {}".format(l, index, maxnum))
