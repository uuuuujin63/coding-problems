def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return
    if x>y:
        parent[x] = y
    else:
        parent[y] = x

def find(parent, x):
    if parent[x]==x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]
    
def solution(n, computers):
    parent = [i for i in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j]==1:
                union(parent, i,j)
    for i in range(n):
        find(parent, i)
    parent = set(parent) 
    answer = len(parent)
    return answer

n = 3
computers = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(solution(n, computers))