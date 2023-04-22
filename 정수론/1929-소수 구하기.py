"""
핵심 아이디어

- 에라토스테네스의 체
"""

import sys
from math import sqrt

input = sys.stdin.readline

m, n = map(int, input().split())

lst = [0] * (n+1)

for i in range(2, n+1):
    lst[i] = i

"""
n의 제곱근 까지만 탐색하는 이유

- n의 제곱근이 x일 때, n = a*b를 만족하는 a와 b 모두 n보다 클 수 없다.
- a가 n보다 크다면 b는 n보다 작아야 한다.
- 즉, n보다 작은 수 가운데 소수가 아닌 수는 항상 n보다 작은 약수를 가진다
- 따라서, 에라토스테네스의 체로 n 이하의 수의 배수를 모두 제거하면 1부터 n 사이의 소수를 구할 수 있다
"""
for i in range(2, int(sqrt(n) + 1)):
    if lst[i] == 0:
        continue
    for j in range(i+i, n+1, i):
        lst[j] = 0

for i in range(m, n+1):
    if lst[i] != 0:
        print(lst[i])