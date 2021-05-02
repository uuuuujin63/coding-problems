import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

dp = [10001]*(k+1)
dp[0] = 0
for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] = min(dp[j], dp[j-coin[i]]+1)

if dp[-1] != 10001:
    print(dp[-1])
else:
    print('-1')