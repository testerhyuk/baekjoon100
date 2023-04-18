"""
핵심 아이디어

1. s와 e를 리스트에 양쪽 끝에 배치한다
2. 기준점 k를 설정한다. k는 리스트의 첫번째 인덱스부터 마지막 인덱스까지다
3. 첫번째 인덱스부터 기준을 잡고 s+e 반복하면서 s와 e가 만날 때까지 첫번째 인덱스와 k를 비교한다
4. 단, 문제에서 "다른 두 수의 합"이라고 했으므로 자기 자신을 포함하면 안된다
"""

import sys

input = sys.stdin.readline

n = int(input())
num = sorted(list(map(int, input().split())))
res = 0

for k in range(n):
    s = 0
    e = n - 1
    while s < e:
        if num[s] + num[e] < num[k]:
            s += 1
        elif num[s] + num[e] > num[k]:
            e -= 1
        else:
            # 문제에서 "다른 두 수의 합"이라고 했으므로 자기 자신은 제외해야 한다
            if s != k and e != k:
                res += 1
                break
            elif s == k:
                s += 1
            elif e == k:
                e -= 1
print(res)