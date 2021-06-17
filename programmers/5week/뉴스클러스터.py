import collections
def solution(str1, str2):
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
    counter1, counter2 = collections.Counter(s1), collections.Counter(s2)
    inter, uni = counter1&counter2, counter2|counter1
    i_s, u_s = sum(x[1] for x in inter.items()), sum(x[1] for x in uni.items())
    if u_s == 0: return 65536
    else: return i_s//u_s*65536

str1 = 'aaa'
str2 = 'AAAA'
print(solution(str1, str2))