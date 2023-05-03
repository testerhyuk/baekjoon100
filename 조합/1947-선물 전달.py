import sys

input = sys.stdin.readline

n = int(input())

d = [0] * 1000001
d[2] = 1

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) * (i-1)
    d[i] = d[i] % 1000000000

print(d[n])