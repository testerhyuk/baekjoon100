import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

computer = [[] for _ in range(n+1)]
answer = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    computer[s].append(e)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        now = q.popleft()

        for i in computer[now]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                q.append(i)

for i in range(1, n+1):
    visited = [False] * (n+1)
    bfs(i)

max_val = max(answer)

for i in range(1, n+1):
    if answer[i] == max_val:
        print(i, end=' ')