#그리디 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())
toping = [0]*n
for i in range(n):
    toping[i] = int(input())
toping.sort(reverse=True)
total = c
t_cnt = 0
res = total//a
while 1:
    for j in range(n):
        total += toping[j]
        t_cnt += 1
        now_res = total//(a+(b*t_cnt))
        if res<=now_res:
            res = now_res
        else:
            print(res)
            exit()
