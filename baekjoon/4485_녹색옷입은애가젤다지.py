import sys
input = sys.stdin.readline
from heapq import heappop, heappush
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1

def bfs():
    dp = [[100000000]*n for _ in range(n)]
    dp[0][0] = arr[0][0]
    v = [[0]*n for _ in range(n)]
    v[0][0] = 1
    hq = []
    heappush(hq, [arr[0][0], 0, 0])
    while hq:
        c, x, y = heappop(hq)
        for i in range(4):
            nowx, nowy = x+dx[i], y+dy[i]
            if 0<=nowx<n and 0<=nowy<n and v[nowx][nowy]==0:
                dp[nowx][nowy] = min(dp[nowx][nowy], dp[x][y]+arr[nowx][nowy])
                heappush(hq, [dp[nowx][nowy], nowx, nowy])
                v[nowx][nowy] = 1
    return dp[-1][-1]

while True:
    n = int(input())
    if n==0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = bfs()
    print('Problem %d: %d'%(cnt, ans))
    cnt += 1

