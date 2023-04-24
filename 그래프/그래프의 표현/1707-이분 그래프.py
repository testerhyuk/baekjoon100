"""
핵심 아이디어

- 트리는 항상 이분 그래프가 된다
- 사이클이 발생하지 않으면 인접 노드와 겹칠일이 없기 때문
- 따라서 사이클이 발생한다면 이분 그래프가 될 수 없다는 의미
"""

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

k = int(input())

def dfs(v):
    global flag

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            answer[i] = (answer[v]+1)%2
            dfs(i)
        elif answer[i] == answer[v]:
            flag = False

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    answer = [0] * (v+1)
    flag = True
    visited = [False] * (v+1)

    for _ in range(e):
        u, vn = map(int, input().split())
        graph[u].append(vn)
        graph[vn].append(u)
    
    for i in range(1, v+1):
        if flag:
            dfs(i)
        else:
            break

    if flag:
        print('YES')
    else:
        print('NO')