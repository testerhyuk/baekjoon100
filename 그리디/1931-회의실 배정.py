"""
핵심 아이디어

- 현재 회의의 종료 시간이 빠를수록 다음 회의와 겹치지 않게 시작하는데 유리하다
- 따라서, 종료 시간이 빠른 순서대로 정렬해 겹치지 않는 회의실을 선택하면 된다
- 단, 종료 시간이 같을 경우 시작 시간이 빠른 순으로 정렬해야 한다
"""

import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n = int(input())
lst = []
cnt = 1

for _ in range(n):
    s, e = map(int, input().split())
    lst.append((s, e))

lst.sort(key=lambda x:(x[1], x[0]))

end = lst[0][1]

for s, e in lst[1:]:
    if end <= s:
        cnt += 1
        end = e

print(cnt)