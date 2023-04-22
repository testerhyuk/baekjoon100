import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
cnt = 0

for _ in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in coin:
    if k//i != 0:
        cnt += (k//i)
        k = k%i
print(cnt)