import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n, m = map(int, input().split())

textList = set([input() for _ in range(n)])
cnt = 0

for _ in range(m):
    subText = input()
    if subText in textList:
        cnt += 1

print(cnt)