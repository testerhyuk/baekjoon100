import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)] # 인접 그래프 초기화
visited = [False] * (n+1) # 방문 체크 리스트 초기화
cnt = 0

for _ in range(m):
    s, e = map(int, input().split())

    # 인접 그래프는 양쪽으로 다 설정
    graph[s].append(e)
    graph[e].append(s)

def dfs(v):
    visited[v] = True # 방문 처리

    # 인접 그래프에 포함된 노드들을 돌면서
    for i in graph[v]:
        # 방문하지 않았다면 해당 노드를 재귀 처리해 해당 노드에 인접 노드로 이동
        if not visited[i]:
            dfs(i)

for i in range(1, n+1):
    # 방문하지 않은 노드만 탐색
    if not visited[i]:
        # 해당 노드를 쭉 돌면서 방문처리를 하기 때문에 여기서 바로 cnt 증가
        cnt += 1
        dfs(i)

print(cnt)