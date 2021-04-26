import sys
input = sys.stdin.readline

def cal(x):
    global res
    global els
    global flg
    if len(x)%2==0:
        for i in range(0, len(x)-1, 2):
            res += x[i]*x[i+1]
    else:
        for i in range(0, len(x)-1, 2):
            res += x[i]*x[i+1]
        if x[-1]<0 and flg == 1:
            res += 0
        else:
            res += x[-1]
    return res

n = int(input())
plus = []
minus = []
els = []
flg = -1
for i in range(n):
    a = int(input())
    if a == 0:
        flg = 1
        els.append(a)
    elif a==1:
        els.append(a)
    elif a>0:
        plus.append(a)
    else:
        minus.append(a)
plus.sort(reverse=True)
minus.sort()
res = 0

cal(plus)
cal(minus)

if len(els)!=0:
    res += sum(els)

print(res)
