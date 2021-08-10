import sys
import copy
input = sys.stdin.readline

sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
arrsm = copy.deepcopy(arr)

def dfs(map, x, y, a, c):
    for i in range(4):
        map[x][y] = c
        nowx, nowy = dx[i]+x, dy[i]+y
        if (0<=nowx<n and 0<=nowy<n):
            if a==map[nowx][nowy]:
                dfs(map, nowx,nowy,a, c)



for i in range(n):
    for j in range(n):
        if arrsm[i][j] == 'R':
            arrsm[i][j] = 'G'

cntsm = 0
cnt = 0

for i in range(n):
    for j in range(n):
        if arrsm[i][j] == 'G' or arrsm[i][j] == 'B':
            cntsm += 1
            dfs(arrsm, i, j,arrsm[i][j],cntsm)
        if arr[i][j] == 'G' or arr[i][j] == 'B' or arr[i][j] == 'R':
            cnt += 1
            dfs(arr, i, j,arr[i][j],cnt)

print(cnt,cntsm)
