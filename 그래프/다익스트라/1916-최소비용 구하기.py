import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
m = int(input())

lst = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [sys.maxsize] * (n+1)
q = PriorityQueue()

for _ in range(m):
    s, e, p = map(int, input().split())
    lst[s].append((e, p))

start, end = map(int, input().split())
distance[start] = 0

q.put((0, start))

while q.qsize() > 0:
    current = q.get()
    c_v = current[1]

    if visited[c_v]:
        continue

    visited[c_v] = True

    for tmp in lst[c_v]:
        next = tmp[0]
        price = tmp[1]

        if distance[next] > distance[c_v] + price:
            distance[next] = distance[c_v] + price
            q.put((distance[next], next))

print(distance[end])