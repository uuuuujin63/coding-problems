import sys
input = sys.stdin.readline

def find(x):
    if parent[x]==x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x!=y:
        if x-y<0:
            parent[y] = x
        else:
            parent[x] = y

v,e = map(int, input().split())

parent = [i for i in range(v+1)]
tree = []
for i in range(e):
    a, b, c = map(int, input().split())
    tree.append([c, a, b])
tree.sort(key=lambda x:x[0])
res = 0
cnt = 0
for i in range(e):
    w = tree[i][0]
    x = tree[i][1]
    y = tree[i][2]
    if find(x)!=find(y):
        union(x, y)
        res += w
        cnt += 1
    if cnt == v-1:
        break
print(res)
