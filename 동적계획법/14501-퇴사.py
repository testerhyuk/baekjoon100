import sys

input = sys.stdin.readline

n = int(input())
t = []
p = []

for _ in range(n):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

t.insert(0, 0)
p.insert(0, 0)

d = [0] * (n+2)

for i in range(n, 0, -1):
    if i + t[i] > n+1:
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1], p[i] + d[i+t[i]])

print(d[1])