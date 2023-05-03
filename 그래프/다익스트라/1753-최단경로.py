import sys
from queue import PriorityQueue

input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())

distance = [sys.maxsize] * (V+1) # 최단 거리 리스트
visited = [False] * (V+1) # 방문 리스트
lst = [[] for _ in range(V+1)] # 인접 리스트
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    lst[u].append((v, w))

q.put((0, k)) # 출발 노드 선택
distance[k] = 0 # 출발 노드 선택

while q.qsize() > 0:
    current = q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True

    for tmp in lst[c_v]:
        next = tmp[0]
        value = tmp[1]

        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print('INF')