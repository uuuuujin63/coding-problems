def union(p, x, y):
    x = find(p, x)
    y = find(p, y)
    if x==y:
        return
    if x>y:
        p[x] = y
    else:
        p[y] = x

def find(p, x):
    if x == p[x]:
        return x
    p[x] = find(p, p[x])
    return p[x]

def solution(n, computers):
    answer = 0
    p = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if computers[i][j] == 1:
                union(p, i, j)
    for i in range(n):
        find(p, i)
    p = set(p)
    answer = len(p)
    return answer