import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n+1):
    graph[i].sort()

def dfs(v):
    print(v, end=' ')

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        now = q.popleft()
        print(now, end=' ')

        # dfs와 다르게 큐에서 꺼낸 값으로 for문
        for i in graph[now]:
            if not visited[i]:
                # bfs는 재귀를 활용하지 않고 while문을 이용하기 때문에 여기서 방문 처리를 해줘야 한다
                visited[i] = True
                q.append(i)

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)