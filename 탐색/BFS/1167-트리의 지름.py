"""
핵심 아이디어

1. 연결된 노드들의 길이를 누적해가면서 거리가 가장 긴 노드의 길이를 구한다
    - (노드, 가중치)의 형태로 인접 리스트 생성
    - 거리 리스트 생성
    - 시작 노드부터 인접 노드로 이동하면서 거리를 거리 리스트에 누적
    - 다 돌고나면 제일 거리가 긴 노드를 시작점으로 두고 반복
    - 거리 리스트에서 가장 큰 값 출력하면 거리가 제일 긴 노드인 지름이 된다
"""

import sys
from collections import deque

input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]
distance = [0] * (v+1)
visited = [False] * (v+1)

for _ in range(v):
    lst = list(map(int, input().split()))

    for i in range(1, len(lst), 2):
        if lst[i] != -1:
            graph[lst[0]].append((lst[i], lst[i+1]))

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                distance[i[0]] = distance[now] + i[1]
                q.append(i[0])

# 시작 노드를 기점으로 돌면서 가장 먼 노드 구함
bfs(1)
max_ = 1

for i in range(2, v+1):
    if distance[i] > distance[max_]:
        max_ = i

distance = [0] * (v+1)
visited = [False] * (v+1)

# 가장 먼 노드에서부터 다시 돌면서 방문하지 않은 노드 방문
bfs(max_)
print(max(distance))