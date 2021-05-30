from itertools import permutations
import math
def solution(numbers):
    answer = 0
    n = len(numbers)
    candis = []
    for i in range(1, n+1):
        per = permutations(numbers, i)
        for j in per:
            candis.append(int("".join(j)))
    candis = set(candis)
    answer = len(candis)
    for candi in candis:
        if candi == 0 or candi == 1:
            answer -= 1
            continue
        for i in range(2, int(math.sqrt(int(candi))+1)):
            if int(candi)%i == 0:
                answer -= 1
                break
    return answer

numbers = "011"
print(solution(numbers))