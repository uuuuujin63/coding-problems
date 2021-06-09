import heapq
def solution(answers):
    answer = []
    hq = []
    so = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    for i in range(3):
        point = 0
        sn = len(so[i])
        for j in range(len(answers)):
            if sn <= j:
                if answers[j] == so[i][j%sn]:
                    point += 1
            else:
                if answers[j] == so[i][j]:
                    point += 1
        heapq.heappush(hq, (-point, i))
    maxn, index = heapq.heappop(hq)
    answer.append(index+1)
    while hq:
        n, nowi = heapq.heappop(hq)
        if n!=maxn:
            break
        else:
            answer.append(nowi+1)
    answer.sort()
    return answer

answers = [1,3,2,4,2]
print(solution(answers))