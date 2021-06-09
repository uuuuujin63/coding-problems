import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while 1:
        a = heapq.heappop(scoville)
        if a>=K:
            break
        if scoville:
            b = heapq.heappop(scoville)
            c = a+b*2
            heapq.heappush(scoville, c)
            answer+=1
        else:
            answer = -1
            break
    return answer

print(solution([1, 1, 1], 4), 2)
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 0, 0], 7), -1)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)