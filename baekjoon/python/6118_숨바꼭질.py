import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dij(hq):
    while(hq):
        wei, vec = heapq.heappop(hq)
        if dist[vec]>wei:
            dist[vec]=wei
            for w, v in aibi[vec]:
                heapq.heappush(hq, (w+wei, v))

N, M = map(int, input().split())
dist = [INF for _ in range(N+1)]
dist[1] = 0
aibi = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    aibi[a].append((1, b))
    aibi[b].append((1, a))

hq = []
for a, b in aibi[1]:
    heapq.heappush(hq, (a, b))

dij(hq)

print(dist.index(max(dist[1:])), max(dist[1:]), dist.count(max(dist[1:])))