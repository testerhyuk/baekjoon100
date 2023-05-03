import sys

input = sys.stdin.readline

n, m = map(int, input().split())
knowTruth = list(map(int, input().split()))
del knowTruth[0]
cnt = 0

party = [[] for _ in range(m)]

for i in range(m):
    party[i] = list(map(int, input().split()))
    del party[i][0]

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

for i in range(m):
    first = party[i][0]
    for j in range(1, len(party[i])):
        union(first, party[i][j])

for i in range(m):
    flag = True
    first = party[i][0]

    for j in range(len(knowTruth)):
        if find(first) == find(knowTruth[j]):
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)