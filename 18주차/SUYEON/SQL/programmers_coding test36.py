# 섬 연결하기
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
    connect = set([costs[0][0]]) # 연결을 확인하는 집합
    
    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
                
    return answer
# 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
# 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.즉, 가장 낮은 가중치를 먼저 선택한다. 사이클을 형성하는 간선을 제외한다. 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가한다.
# 먼저 비용을 기준으로 costs를 오름차순으로 정렬한다. connect는 연결된 섬을 확인하는 집합입니다. 섬이 중복되면 안되므로 리스트가 아닌 집합을 사용한다. 그 다음 Kruskal 알고리즘을 통해 최소 비용을 구한다. 반복문으로 costs를 돌면서 두 섬이 connect에 있으면 넘어가고 두 섬 중 하나만 있는 경우 두 섬을 connect에 추가해주고 answer에 비용을 추가한다. 

