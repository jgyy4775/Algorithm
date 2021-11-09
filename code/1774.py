import sys
from math import sqrt
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
pos, road, edges = [0]*(n+1), [], []
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
result = 0

for i in range(1, n+1):
    x, y = map(int, sys.stdin.readline().split())
    pos[i] = (x, y)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    road.append((a, b))
    union_parent(parent, a, b)

for i in range(1, n):
    for j in range(i+1, n+1):
        edges.append((sqrt((pos[i][0]-pos[j][0])**2 + (pos[i][1]-pos[j][1])**2)
                      , i, j))

edges.sort()
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
print('%.2f' %(result))
