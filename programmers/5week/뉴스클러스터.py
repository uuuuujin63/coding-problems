def solution(str1, str2):
    answer = 1
    uni = 0
    inter = 0
    s1 = []
    s2 = []
    str1 = str1.upper()
    str2 = str2.upper()
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            s1.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if str2[j:j+2].isalpha():
            s2.append(str2[j:j+2])
    for ss1 in s1:
        for ss2 in s2:
            if ss1==ss2:
                inter += 1
    uni = len(s1)+len(s2)-inter
    if uni == 0 and inter == 0:
        return 65536
    answer = int(inter/uni*65536)
    return answer

str1 = '12444'
str2 = '4456788'
print(solution(str1, str2))