# 너비 우선 탐색 (BFS)

- 시작 노드에서 출발해 시작 노드를 기준으로 가까운 노드를 먼저 방문하면서 탐색하는 알고리즘
- 큐 이용
- FIFO 탐색
- 탐색 시작 노드와 가까운 노드를 우선해 탐색하기 때문에 최단 경로를 보장한다

<br><br>

## BFS 초기 작업 및 풀이 순서
- 인접 리스트 초기화
- 방문 리스트 초기화
- 시작 노드 큐에 삽입
- 큐에서 노드를 꺼내고 인접 노드를 다시 큐에 삽입
- 큐에 값이 없을 때까지 반복