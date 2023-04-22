import sys
from math import sqrt

input = sys.stdin.readline

n = int(input())

lst = [0] * 10000001

for i in range(2, 10000001):
    lst[i] = i

for i in range(2, int(sqrt(10000001))):
    if lst[i] == 0:
        continue
    for j in range(i+i, 10000001, i):
        lst[j] = 0

for i in range(n, 10000001):
    if lst[i] != 0 and lst[i] == int(str(lst[i])[::-1]):
        print(lst[i])
        break