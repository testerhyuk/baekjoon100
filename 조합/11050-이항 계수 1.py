import sys

input = sys.stdin.readline

n, k = map(int, input().split())

lst = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    lst[i][1] = i
    lst[i][0] = 1
    lst[i][i] = 1

for i in range(2, n+1):
    for j in range(1, i):
        lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

print(lst[n][k])