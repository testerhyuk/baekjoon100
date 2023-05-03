import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

d = [0] * (n+1) # 진입 차수 리스트
lst = [[] for _ in range(n+1)] # 인접 리스트

q = deque()

# 인접 리스트 생성
for _ in range(m):
    h1, h2 = map(int, input().split())
    d[h2] += 1
    lst[h1].append(h2)

# 차수가 0인 값만 큐에 삽입
for i in range(1, n+1):
    if d[i] == 0:
        q.append(i)

# 위상 정렬 수행
while q:
    now = q.popleft()
    print(now, end=' ')
    for i in lst[now]:
        d[i] -= 1
        if d[i] == 0:
            q.append(i)