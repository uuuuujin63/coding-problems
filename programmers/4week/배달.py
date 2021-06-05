from collections import deque
def solution(N, road, K):
    answer = 0
    town = [[] for _ in range(N+1)]
    for i, j, cost in road:
        town[i].append([j, cost])
        town[j].append([i, cost])
    q = deque()
    visit = []
    for i, cost in town[1]:
        if cost<=K:
            q.append([i, cost])
    while q:
        x, cost = q.popleft()
        if x not in visit:
            visit.append(x)
        for i in range(1, N+1):
            for j in range(len(town[x])):
                if town[x][j][0] == i:
                    if cost+town[x][j][1]<=K:
                        q.append([i, cost+town[x][j][1]])
    answer = len(visit)
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))