import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

from collections import deque


n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

count = []
v = [[0]*m for _ in range(n)]


def bfs(i, j):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([i, j])
    v[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nowx, nowy = x+dx[k], y+dy[k]
            if 0<=nowx<n and 0<=nowy<m :
                if arr[nowx][nowy] == 1 and v[nowx][nowy] == 0:
                    q.append([nowx,nowy])
                    v[nowx][nowy] = 1
                    cnt += 1
    count.append(cnt)

for i in range(n):
    for j in range(m):
        if(arr[i][j]==1 and v[i][j]==0):
            cnt = 1
            bfs(i, j)
if(len(count)==0):
    print(len(count))
    print(0)
else:
    print(len(count))
    print(max(count))