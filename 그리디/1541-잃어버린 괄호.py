"""
핵심 아이디어

- 값을 최소로 만들어야 하므로 "-"를 기준으로 나눈 후 각각의 원소들을 더하고 최종적으로 빼면 된다
"""

import sys

input = sys.stdin.readline

op = list(map(str, input().split('-')))
res = []

for i in op:
    res.append(sum(map(int, i.split('+'))))

sum = res[0]

for i in res[1:]:
    sum -= i

print(sum)