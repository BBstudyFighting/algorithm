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
