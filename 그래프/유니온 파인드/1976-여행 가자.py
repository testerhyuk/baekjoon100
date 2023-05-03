import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

connection = [[0 for _ in range(1, n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    connection[i] = list(map(int, input().split()))
    connection[i].insert(0, 0)

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

for i in range(1, n+1):
    for j in range(1, n+1):
        if connection[i][j] == 1:
            union(i, j)

route = list(map(int, input().split()))
route.insert(0,0)

first = find(route[1])
flag = True

for i in range(2, len(route)):
    if find(route[i]) != first:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')