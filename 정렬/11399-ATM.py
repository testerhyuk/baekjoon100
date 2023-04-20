import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst2 = []

for i, v in enumerate(lst):
    lst2.append((i, v))
lst2.sort(key=lambda x : x[1])
psum = [0] * (n+1)

for i in range(1, n+1):
    psum[i] = psum[i-1] + lst2[i-1][1]

print(sum(psum))