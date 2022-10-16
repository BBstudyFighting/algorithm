# 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
# answer : 경과시간
# bridge : 다리 길이와 같은 길이의 값이 0으로 된 리스트 생성
    
    while bridge:
        
        answer += 1
        bridge.pop(0)
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
                 
         
    return answer

# 트럭이 다리를 지나는 과정을 answer+=1을 통해 경과시간 계산

# bridge 리스트 안 (즉 다리 위에 있느 트럭의 총 무게)과 다음 대기열에 있는 트럭 무게가 다리가 감당할 수 있는 총 무게 (weight) 을 넘지 않는 조건을 만족하면 다음 트럭을 리스트에 추가한다
# 만족을 하지 못한다면 0을 추가하여 다리의 길이를 유지
# 트럭의 대기열의 길이가 0이 되면 내부 반복문 종료
# bridge 리스트의 길이가 0이 되면 반복문 종료후 경과시간 (answer) 리턴