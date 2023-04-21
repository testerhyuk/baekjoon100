"""
핵심 아이디어

- start = 0, end = len(lst) - 1
- mid = (start + end) // 2
- 시작점이 마지막 지점보다 작은 동안 반복
- 중간 지점 > 타깃 -> end = mid - 1
- 중간 지점 < 타깃 -> start = mid + 1
"""

import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n = int(input())
lst_n = list(map(int, input().split()))
m = int(input())
lst_m = list(map(int, input().split()))
lst_n.sort()

for i in range(m):
    start = 0
    end = len(lst_n) - 1
    find = False

    # 시작점이 마지막 지점보다 작은 동안에만
    while start <= end:
        mid = (start + end) // 2

        if lst_m[i] < lst_n[mid]:
            end = mid - 1
        elif lst_m[i] > lst_n[mid]:
            start = mid + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)