from collections import deque

def solution(n, edge):
    answer = 0
    node = [[]*(n+1) for _ in range(n+1)]
    for a, b in edge:
        node[a].append(b)
        node[b].append(a)
    v = [(-1) for _ in range(n+1)]
    q = deque([[1, 0]]) #시작, 카운트
    v[1] = 0
    while q:
        nowq, cnt = q.popleft()
        for i in node[nowq]:
            if (v[i]==-1):
                q.append([i, cnt+1])
                v[i] = cnt+1;
    mn = max(v)

    for i in v:
        if (i == mn):
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))