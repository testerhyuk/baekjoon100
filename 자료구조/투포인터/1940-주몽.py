"""
# 투 포인터 이동 원칙(두 개만 더해갈 때)
- start = 0
- end = n-1
1. start + end > n -> end -= 1
2. start + end < n -> start += 1
3. start + end == n -> start+=1, end-=1, count+=1
"""

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

# 재료는 고유 번호를 지니므로 가장 작은 값과 가장 큰 값부터 시작하기 위해 정렬
material = sorted(list(map(int, input().split())))

s = 0
e =  n-1
cnt = 0

while s < e:
    # 합이 작다면 작은 쪽을 올려야 합이 커짐
    if material[s] + material[e] < m:
        s += 1
    # 합이 크다면 큰 쪽을 줄여야 합이 줄어듬
    elif material[s] + material[e] > m:
        e -= 1
    # 합이 같다면 양쪽 인덱스 각각 변경
    else:
        cnt += 1
        e -= 1
        s += 1
print(cnt)