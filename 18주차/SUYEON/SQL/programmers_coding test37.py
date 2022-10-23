# 단속카메라
# 카메라를 만났는지에 대한 Check 배열을 만들고 각 구간을 모두 검사하는 방법
def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    leng = len(routes)
    checked = [0] * leng

    for i in range(leng):
        if checked[i] == 0:
            camera = routes[i][1] # 진출 지점에 카메라를 갱신
            answer += 1
        for j in range(i+1, leng):
            if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
                checked[j] = 1
    return answer
# 진출 지점 기준으로 정렬 후 카메라에 걸리는 지 확인하는 방법
    # 진출 지점에 카메라를 설치하는 이유는 다음 구간의 차량의 진입 시점과 비교하면 설치한 카메라에 걸리는 지 O(N)으로 확인이 가능하다
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer
# 진출 지점 기준으로 오름 차순 정렬합니다. (routes[1] 기준)
# 최대 -30000이니 초기 카메라 위치를 -30001로 초기화 해줍니다.
# routes 배열을 반복하면서 카메라가 진입 지점(route[0])보다 작은지 확인합니다.
# 작다면, 현재 카메라 위치로 해당 차량을 만나지 못했다는 의미이니
# 4-1. 카메라를 추가로 세우고
# 4-2. 가장 최근 카메라의 위치(route[1])를 갱신합니다.