# 탐색

<br><br>

## 깊이 우선 탐색(DFS)
- 그래프의 시작 노드에서 출발해 탐색할 한 쪽 분기를 정해 최대 깊이까지 탐색을 마친 후 다른 쪽 분기로 이동해 다시 탐색하는 알고리즘
- 재귀 함수로 구현 or 스택 이용
- O(V + E) 시간 복잡도 -> V : 노드 수, E : 엣지 수
- 한 번 방문한 노드를 다시 방문하면 안되므로 체크 리스트가 필요

<br><br>

### DFS 초기 작업
- 인접 리스트로 그래프 표현
- 방문 리스트 초기화
- 시작 노드 스택에 삽입

<br><br>

### DFS 풀이 순서

1. 스택에 시작 노드 삽입 후 해당 위치의 방문 리스트 체크
2. 스택에서 노드를 꺼낸 후 인접 노드를 다시 스택에 삽입
3. 스택에 값이 없을 때까지 반복

<br><br>

## 너비 우선 탐색 (BFS)

- 시작 노드에서 출발해 시작 노드를 기준으로 가까운 노드를 먼저 방문하면서 탐색하는 알고리즘
- 큐 이용
- FIFO 탐색
- 탐색 시작 노드와 가까운 노드를 우선해 탐색하기 때문에 최단 경로를 보장한다

<br><br>

### BFS 초기 작업 및 풀이 순서
- 인접 리스트 초기화
- 방문 리스트 초기화
- 시작 노드 큐에 삽입
- 큐에서 노드를 꺼내고 인접 노드를 다시 큐에 삽입
- 큐에 값이 없을 때까지 반복

<br><br>

## 이진 트리
- 정렬 데이터에서 원하는 데이터를 탐색할 때 사용

<br><br>

### 핵심 이론
- 현재 데이터셋의 중앙값 선택
- 중앙값 > 타깃값이면 중앙값 기준 왼쪽 데이터셋 선택
- 중앙값 < 타깃값이면 중앙값 기준 오른쪽 데이터셋 선택
- 반복하면서 중앙값 == 타깃값이면 탐색 종료

<br><br>

| 다시 풀어볼 문제 | Tag                          | 태그                | 문제번호    | 문제이름    | 난이도    | 문제풀이    |
| :------:  | :--------------------------: | :-----------------: | :------:  | :------:  |  :------:  | :------:  |
| :heavy_check_mark: | DFS | 깊이 우선 탐색 | <a href="https://www.acmicpc.net/problem/11724">11724</a> | <a href="https://www.acmicpc.net/problem/11724">연결 요소의 개수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | [바로가기](./11724-연결%20요소의%20개수.py) |
| :heavy_check_mark: | DFS | 깊이 우선 탐색 | <a href="https://www.acmicpc.net/problem/2023">2023</a> | <a href="https://www.acmicpc.net/problem/2023">신기한 소수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | [바로가기](./2023-신기한%20소수.py) |
| :heavy_check_mark: | DFS | 깊이 우선 탐색 | <a href="https://www.acmicpc.net/problem/13023">13023</a> | <a href="https://www.acmicpc.net/problem/13023">ABCDE</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | [바로가기](./13023-ABCDE.py) |
|  | BFS | 너비 우선 탐색 | <a href="https://www.acmicpc.net/problem/1260">1260</a> | <a href="https://www.acmicpc.net/problem/1260">DFS와 BFS</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | [바로가기](./1260-DFS와%20BFS.py) |
| :heavy_check_mark: | BFS | 너비 우선 탐색 | <a href="https://www.acmicpc.net/problem/2178">2178</a> | <a href="https://www.acmicpc.net/problem/2178">미로 탐색</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | [바로가기](./2178-미로%20탐색.py) |
| :heavy_check_mark: | BFS | 너비 우선 탐색 | <a href="https://www.acmicpc.net/problem/1167">1167</a> | <a href="https://www.acmicpc.net/problem/1167">트리의 지름</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> | [바로가기](./1167-트리의%20지름.py) |
| :heavy_check_mark: | Binary Search | 이진 탐색 | <a href="https://www.acmicpc.net/problem/1920">1920</a> | <a href="https://www.acmicpc.net/problem/1920">수 찾기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | [바로가기](./1920-수%20찾기.py) |
| :heavy_check_mark: | Binary Search | 이진 탐색 | <a href="https://www.acmicpc.net/problem/2343">2343</a> | <a href="https://www.acmicpc.net/problem/2343">기타 레슨</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | [바로가기](./2343-기타%20레슨.py) |
| :heavy_check_mark: | Binary Search | 이진 탐색 | <a href="https://www.acmicpc.net/problem/1300">1300</a> | <a href="https://www.acmicpc.net/problem/1300">k번째 수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> | [바로가기](./1300-k번째%20수.py) |