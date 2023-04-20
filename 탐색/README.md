# 탐색

<br><br>

## 깊이 우선 탐색(DFS)
- 그래프의 시작 노드에서 출발해 탐색할 한 쪽 분기를 정해 최대 깊이까지 탐색을 마친 후 다른 쪽 분기로 이동해 다시 탐색하는 알고리즘
- 재귀 함수로 구현 or 스택 이용
- O(V + E) 시간 복잡도 -> V : 노드 수, E : 엣지 수
- 한 번 방문한 노드를 다시 방문하면 안되므로 체크 리스트가 필요

### DFS 초기 작업
- 인접 리스트로 그래프 표현
- 방문 리스트 초기화
- 시작 노드 스택에 삽입

### DFS 풀이 순서

1. 스택에 시작 노드 삽입 후 해당 위치의 방문 리스트 체크
2. 스택에서 노드를 꺼낸 후 인접 노드를 다시 스택에 삽입
3. 스택에 값이 없을 때까지 반복

<br><br>

| 다시 풀어볼 문제 | Tag                          | 태그                | 문제번호    | 문제이름    | 난이도    | 문제풀이    |
| :------:  | :--------------------------: | :-----------------: | :------:  | :------:  |  :------:  | :------:  |
| :heavy_check_mark: | DFS | 깊이 우선 탐색 | <a href="https://www.acmicpc.net/problem/11724">11724</a> | <a href="https://www.acmicpc.net/problem/11724">연결 요소의 개수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | [바로가기](./탐색/11724-연결%20요소의%20개수.py) |
| :heavy_check_mark: | DFS | 깊이 우선 탐색 | <a href="https://www.acmicpc.net/problem/2023">2023</a> | <a href="https://www.acmicpc.net/problem/2023">신기한 소수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | [바로가기](./탐색/2023-신기한%20소수.py) |
| :heavy_check_mark: | DFS | 깊이 우선 탐색 | <a href="https://www.acmicpc.net/problem/13023">13023</a> | <a href="https://www.acmicpc.net/problem/13023">ABCDE</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | [바로가기](./탐색/13023-ABCDE.py) |