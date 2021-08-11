import sys,heapq
input = sys.stdin.readline

INF = int(1e9)
a, b = map(int, input().split())
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

dist = [INF]*(n+1)
dist[a] = 0
q = []
heapq.heappush(q, (0, a))

while q:
    d, c = heapq.heappop(q)
    if(dist[c]<d):
        continue

    for next in arr[c]:
        if dist[next] > d+1:#현재 온 가중치보다 저장되어있는게 크다면 현재 가중치 넣어줌
            dist[next] = d+1
            heapq.heappush(q, (d+1, next))

if dist[b] == INF:
    print(-1)
else:
    print(dist[b])