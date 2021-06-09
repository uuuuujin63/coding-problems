def solution(name):
    answer = 0
    name = list(name)
    base = ["A"]*len(name)
    idx = 0
    while 1:
        r = 1
        l = 1
        if name[idx]!="A":
            answer += min(ord("Z")-ord(name[idx])+1, ord(name[idx])-ord("A"))
            name[idx] = "A"
        if name == base:
            break
        else:
            for i in range(1, len(name)):
                if name[idx+i] == "A":
                    r += 1
                else:
                    break
                if name[idx-i] == "A":
                    l += 1
                else:
                    break
            if r>l:
                answer += l
                idx -=l
            else:
                answer += r
                idx += r
    return answer

name = "JEROEN"
print(solution(name))