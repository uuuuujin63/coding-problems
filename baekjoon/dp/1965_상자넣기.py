import sys
input = sys.stdin.readline

n = int(input())
boxs = [0]+list(map(int, input().split()))

dp = [0]

for box in boxs:
    if dp[-1]<box:
        dp.append(box)
    else:
        left = 0
        right = len(dp)
        while left<right:
            mid = (left+right)//2
            if dp[mid]<box:
                left = mid+1
            else:
                right = mid
        dp[right]=box

print(len(dp)-1)


