def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x==y:
        return
    parent[x] = y

def find(parent, x):
    if parent[x]==x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def solution(n, costs):
    answer = 0
    cnt = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x:x[2])
    for i in range(len(costs)):
        if find(parent, costs[i][0])!=find(parent, costs[i][1]):
            union(parent, costs[i][0], costs[i][1])
            answer += costs[i][2]
            cnt += 1
        if cnt == n:
            return answer
    return answer
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))