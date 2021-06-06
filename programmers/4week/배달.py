import heapq
def solution(N, road, K):
    answer = 0
    town = [[] for _ in range(N+1)]
    for i, j, cost in road:
        town[i].append([j, cost])
        town[j].append([i, cost])
    sorted(town)
    q = []
    visit = []
    for i, cost in town[1]:
        if cost<=K:
            heapq.heappush(q, [i, cost])
    print(q)
    while q:
        print(q)
        x, cost = heapq.heappop(q)
        if x not in visit:
            visit.append(x)
        for nowx, nowc in town[x]:
            if cost+nowc <= K:
                heapq.heappush(q, [nowx, cost+nowc])
        if len(visit) == N-1:
            return len(visit)
    answer = len(visit)
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))