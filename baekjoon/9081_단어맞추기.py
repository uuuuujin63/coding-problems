import sys
input = sys.stdin.readline
def next_word(case):
    for i in range(len(case)-1,0,-1):
        for j in range(i-1, -1, -1):
            for k in range(i-j): #i를 움직이면서 i와j사이도 봐주기 위해서
                if case[j]<case[i-k]:
                    tmp = case[j]
                    case[j] = case[i-k]
                    case[i-k] = tmp
                    if j!=len(case)-1:
                        temp = case[j+1:]
                        temp.sort()
                        print(''.join(case[:j+1]+temp))
                    return
    print(''.join(map(str, case)))
    return
n = int(input())
for _ in range(n):
    case = list(map(str, input().rstrip()))
    next_word(case)
   
