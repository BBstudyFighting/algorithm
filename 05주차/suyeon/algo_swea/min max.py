'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

입력
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

출력
#1 630739
#2 740510
#3 838110

'''

T = int(input()) # 테스트 갯수(3)를 input하고 int로 변경

for tc in range(1, T+1): # range(1,4): 1이상 4미만
    N = int(input()) # nums의 총 갯수 
    nums = list(map(int, input().split())) 
    # nums에 포함된 숫자들을 input하고 공백 기준으로 나누어 int로 바꾸고 리스트형식으로 변경
    answer = max(nums) - min(nums)
		# 문제에서 가장 큰 수와 가장 작은 수의 차이를 물어봤기 때문에 max(nums) - min(nums)로 작성

    # 최종 출력 예시
    print('#{} {}'.format(tc, answer))
		# print(f'#{tc} {answer}') # 요즘 포매팅 방식
		# print('#{} {}'.format(tc, answer)) #옛날 포매팅 방식
