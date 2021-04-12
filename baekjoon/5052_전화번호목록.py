import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    flg = "YES"
    arr = []
    for _ in range(n):
        arr.append(input().rstrip('\n'))
    arr.sort()
    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            flg = "NO"
            break
    print(flg)
