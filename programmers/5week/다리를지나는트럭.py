from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque([0]*bridge_length)

    while q:
        answer += 1
        q.popleft()
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop())
            else:
                q.append(0)
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))