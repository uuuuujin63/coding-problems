import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))

arr.sort()

start = 1
end = arr[n-1]-arr[0]
res = 0
while(start <= end):
    mid = (start+end)//2
    tmp = arr[0]+mid
    cnt = 1
    for i in range(1, n):
        if(tmp <= arr[i]):
            cnt += 1
            tmp = arr[i]+mid
    if(cnt >= m):
        start = mid+1
        res = max(res, mid)
    else:
        end = mid-1

print(res)
