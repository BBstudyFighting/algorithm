# 디스크 컨트롤러
# 1. jobs 배열은 소요시간을 기준으로 오름차순 정렬을 한다. 소요시간이 작을수록 각 작업들이 기다리는 시간이 줄어들기 때문이다.
# 2. jobs 배열이 empty가 될때까지 while문을 돌린다.
# 3. jobs 길이만큼 for문을 돌리면서 해당 작업의 요청시간이 start(현재까지 진행된 작업 시간)보다 작으면,
#   즉, 해당 작업이 진행된 시간보다 먼저 요청이 들어왔으면, 해당 작업을 진행시키고 jobs 배열에서 지워버린다.
def solution(jobs):
    answer = 0
    start = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    return answer // length
#################################################
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)