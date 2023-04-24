import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
cityList = [[] for _ in range(n+1)] # 인접 리스트 생성
visited = [-1] * (n+1)
answer = []

for _ in range(m):
    s, e = map(int, input().split())
    cityList[s].append(e)

def bfs(v):
    visited[v] += 1
    q = deque()
    q.append(v)

    while q:
        now = q.popleft()
        for i in cityList[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.append(i)

bfs(x)

for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)