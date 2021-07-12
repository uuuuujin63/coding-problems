def solution(clothes):
    answer = 1
    dic = {}
    for name, c in clothes:
        if c in dic.keys():
            dic[c] += 1
        else:
            dic[c] = 2
    for n in dic.values():
        answer *= n
    return answer-1