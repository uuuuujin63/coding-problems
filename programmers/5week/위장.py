def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes:
        if c[1] in dic.keys():
            dic[c[1]] += 1
        else:
            dic[c[1]] = 2
    for i in dic.values():
        answer *= i
    answer -= 1
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))