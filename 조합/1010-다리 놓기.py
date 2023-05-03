import sys

input = sys.stdin.readline

T = int(input())

d = [[0 for _ in range(30)] for _ in range(30)]

for i in range(30):
    d[i][0] = 1
    d[i][1] = i
    d[0][i] = 1

for i in range(2, 30):
    for j in range(1, 30):
        d[i][j] = d[i-1][j-1] + d[i-1][j]

for _ in range(T):
    n, m = map(int, input().split())
    print(d[m][n])