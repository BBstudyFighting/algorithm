'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
''''

T = int(input())
for test_case in range(1, T + 1):
    #K: 이동 가능한 거리, N: 종점 정류장, M: 충전소 개수
    K, N, M = map(int, input().split(" "))
    #stations: 충전 가능 정류장 정보
    stations= tuple(map(int, input().split(" ")))
    

    now = 0
    can_go = now+K
    charge_station = 0
    count = 0
    
    while (can_go<N):
        for i in stations:
            if now < i <= can_go:
                charge_station = i
            elif can_go < i:
                break

        if charge_station == -1:
            count = 0
            break

        now = charge_station
        can_go = now+K
        count += 1
        charge_station = -1
        
    print(f"#{test_case} {count}")
    
#####################
# 테스트 케이스 수 입력
T = int(input())

# T만큼 테스트 케이스 반복
for tc in range(1, T+1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수, N : 종점 정류장, M : 충전기가 설치된 정류장 개수
    K, N, M = list(map(int, input().split()))

    # 충천지가 설치된 정류장 리스트 입력
    charge_station = list(map(int, input().split()))
    # 충전 횟수 count와 현재 위치 current 변수 초기화
    count = current = 0

    # 종점에 도착할 때까지 반복
    while current + K < N:
        # K 범위 안에서 현 위치를 조정하면서 이동
        for step in range(K, 0, -1):
            # 현재 위치 + 이동 거리만큼 이동했을 때 충전기가 있는 정류장일 경우
            if (current + step) in charge_station:
                # 현재 위치를 변경
                current += step
                # 충전 횟수 +1
                count += 1
                # for 문을 종료
                break
        # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우 count를 0으로 하고 while문을 종료
        else:
            count = 0
            break

    # 결과 출력
    print('#{} {}'.format(tc, count))
