import sys

input = sys.stdin.readline

T = int(input())

d = [[0 for _ in range(15)] for _ in range(15)]

for i in range(1, 15):
    d[i][1] = 1
    d[0][i] = i

for i in range(1, 15):
    for j in range(2, 15):
        d[i][j] = d[i][j-1] + d[i-1][j]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(d[k][n])