"""
# 투 포인터 이동 원칙

- 더해갈 수 sum = A[0]
- start = 0, end = 0
- sum > n
    1. sum -= start
    2. start += 1
- sum < n
    1. end += 1
    2. sum += end
- sum == n
    1. end += 1
    2. sum += end
    3. count += 1
"""

import sys

input = sys.stdin.readline

n = int(input())

s = 1
e = 1
ans = 1 # ans 값을 1로 초기화 하는 이유는 n이 15일 때 15만 뽑는 경우의 수를 미리 넣고 초기화하기 때문
sum = 1

while e != n:
    if sum < n:
        e += 1
        sum += e
    elif sum > n:
        sum -= s
        s += 1
    else:
        ans += 1
        e += 1
        sum += e

print(ans)