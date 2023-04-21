"""
핵심 아이디어

- 네 방향으로 조건을 확인
- 조건이 맞으면 가려는 방향에 현재 방향의 값 + 1 대입
- 즉, 이동할 때마다 이동 횟수를 가려는 방향에 대입하면서 이동 횟수를 체크
- graph[n-1][m-1]에는 이동한 횟수 값이 담겨있으므로 출력
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
direction_x = [1, 0, -1, 0] # x 방향
direction_y = [0, 1, 0, -1] # y 방향

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        now_x, now_y = q.popleft()

        for i in range(4):
            x = now_x + direction_x[i] # 다음 x 방향
            y = now_y + direction_y[i] # 다음 y 방향
            if 0 <= x < n and 0 <= y < m and graph[x][y] == 1 and not visited[x][y]:
                # 조건 만족시 방문 처리
                visited[x][y] = True
                # 다음 방향에 이동횟수 추가
                graph[x][y] = graph[now_x][now_y] + 1
                # 다음 방향을 q에 추가해서 다다음 방향으로 이동
                q.append((x, y))

bfs(0, 0)
print(graph[n-1][m-1])