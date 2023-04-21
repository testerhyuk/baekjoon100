import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
arrive = False

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v, c):
    global arrive

    # 깊이가 5면 중지
    if c == 5:
        arrive = True
        return
    
    visited[v] = True
    
    # 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행
    for i in graph[v]:
        if not visited[i]:
            dfs(i, c + 1)
    
    # 백트래킹을 하므로 방문하지 않은 걸로 다시 처리해줘야 한다
    visited[v] = False

# 모든 노드를 돌면서 관계 확인해야 하므로 n만큼 for문
for i in range(n):
    dfs(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)