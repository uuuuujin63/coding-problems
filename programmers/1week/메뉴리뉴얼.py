from itertools import combinations
def solution(orders, course):
    answer = []
    for cou in course:
        candi = {}
        for order in orders:
            combi = combinations(sorted(order), cou)
            for c in combi:
                if c in candi:
                    candi[c] += 1
                else:
                    candi[c] = 1
        candi = sorted(candi.items(), reverse=True, key=lambda item:item[1])
        for i in range(len(candi)):
            if candi[i][1] == candi[0][1] and candi[i][1]>=2:
                answer.append(''.join(candi[i][0]))
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))