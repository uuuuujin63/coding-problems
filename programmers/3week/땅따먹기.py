def solution(land):
    answer = 0
    dp = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(len(land[0])):
            if i == 0:
                dp[i][j] = land[i][j]
                continue
            else:
                for k in range(len(land[0])):
                    if j == k:
                        continue
                    dp[i][j] = max(dp[i][j], dp[i-1][k]+land[i][j])
    answer = max(dp[-1])
    return answer

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))