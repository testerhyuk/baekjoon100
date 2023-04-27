# 그래프

<br><br>

| 다시 풀어볼 문제 | Tag                          | 태그                | 문제번호    | 문제이름    | 난이도    | 문제풀이    |
| :------:  | :--------------------------: | :-----------------: | :------:  | :------:  |  :------:  | :------:  |
| :heavy_check_mark: | Graph | 그래프 | <a href="https://www.acmicpc.net/problem/18352">18352</a> | <a href="https://www.acmicpc.net/problem/18352">특정 거리의 도시 찾기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | [바로가기](./그래프의%20표현/18352-특정%20거리의%20도시%20찾기.py) |
| :heavy_check_mark: | Graph | 그래프 | <a href="https://www.acmicpc.net/problem/1325">1325</a> | <a href="https://www.acmicpc.net/problem/1325">효율적인 해킹</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | [바로가기](./그래프의%20표현/1325-효율적인%20해킹.py) |
| :heavy_check_mark: | Graph | 그래프 | <a href="https://www.acmicpc.net/problem/1707">1707</a> | <a href="https://www.acmicpc.net/problem/1707">이분 그래프</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | [바로가기](./그래프의%20표현/1707-이분%20그래프.py) |
| :heavy_check_mark: | Graph | 그래프 | <a href="https://www.acmicpc.net/problem/2251">2251</a> | <a href="https://www.acmicpc.net/problem/2251">물통</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | [바로가기](./그래프의%20표현/2251-물통.py) |
| :heavy_check_mark: | Graph | 유니온 파인드 | <a href="https://www.acmicpc.net/problem/1717">1717</a> | <a href="https://www.acmicpc.net/problem/1717">집합의 표현</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | [바로가기](./유니온%20파인드/1717-집합의%20표현.py) |

## 핵심 내용

<br><br>

### 2차원 리스트 생성

<br><br>

- 추천 방법
    - A = [[0 for col in range(4)] for row in range(3)]

- 추천하지 않는 방법
    - A = [[0] * 4] * 3
    - 얕은 복사를 일으켜 생성하는 방법이기 때문에
    - 위와 같은 방식으로 선언 후 변경하면 다른 원소의 값도 함께 변경될 수 있다
    - A[0][0]의 값을 1로 변경하면 A[1][0], A[2][0]도 함께 변경된다

<br><br>

### 에지 리스트

<br><br>

- 에지 리스트는 리스트에 출발 노드, 도착 노드, 가중치를 저장해 에지를 표현한다

<br><br>

#### 가중치 없는 그래프

<br><br>

- 가중치가 없는 그래프는 출발 노드와 도착 노드만 표현하므로 리스트의 열은 2개면 충분하다
- 1에서 2로 뻗어나가는 에지는 [1, 2]로 표현한다. 마찬가지로, 4에서 5로 뻗어나가는 에지는 [4, 5]로 표현한다
- 이처럼 방향이 있는 그래프는 순서에 맞게 노드를 리스트에 저장하는 방식으로 표현한다
- 만약 방향이 없다면 1에서 2로 뻗어나가는 에지는 [1, 2], [2, 1]과 같이 표현한다

<br><br>

#### 가중치 있는 그래프

<br><br>

- 가중치가 있는 그래프는 열을 3개로 늘려 3번째 열에 가중치를 저장한다
- 1에서 2로 향하는 가중치가 8인 에지는 [1, 2, 8]로 표현한다

<br><br>

### 인접행렬

<br><br>

#### 가중치 없는 인접 행렬

<br><br>

<img src='https://github.com/testerhyuk/notes/blob/main/%EC%9D%B8%EC%A0%91%ED%96%89%EB%A0%AC.jpg?raw=true'>

<br><br>

#### 가중치 있는 인접 행렬

<br><br>

<img src='https://github.com/testerhyuk/notes/blob/main/%EA%B0%80%EC%A4%91%EC%B9%98%EC%9D%B8%EC%A0%91%ED%96%89%EB%A0%AC.PNG?raw=true'>

<br><br>

### 인접 리스트

<br><br>

- 인접 행렬에서 노드 개수에 비해 에지가 적을 때 공간 효율성이 떨어지는 문제를 보완함
- 인접 리스트는 노드 개수만큼 리스트를 선언해서 그래프를 표현한다

<br><br>

#### 가중치 없는 인접 리스트

<br><br>

<img src='https://github.com/testerhyuk/notes/blob/main/%EC%9D%B8%EC%A0%91%EB%A6%AC%EC%8A%A4%ED%8A%B8.PNG?raw=true'>

<br><br>

- n번 노드와 연결되어 있는 노드를 리스트의 index n에 연결된 노드 개수만큼 리스트에 append하는 방식으로 표현한다
- 예를 들어, 노드 1과 연결된 2, 3 노드는 A[1]에 [2, 3]을 연결하는 방식으로 표현한다

<br><br>

#### 가중치 있는 인접 리스트

<br><br>

<img src='https://github.com/testerhyuk/notes/blob/main/%EC%9D%B8%EC%A0%91%EB%A6%AC%EC%8A%A4%ED%8A%B8%EA%B0%80%EC%A4%91%EC%B9%98.PNG?raw=true'>

<br><br>

- 가중치가 있는 경우 input data를 2개(도착 노드, 가중치)로 사용한다
- A[1]에 [(2, 8), (3, 3)]이 연결되어 있다. 이는 노드 1과 2가 가중치 8 에지로, 노드 1과 3이 가중치 3 에지로 연결되어 있다는 것을 보여준다
- 코딩 테스트에서는 인접 리스트로 구현하는 것이 효율성이 좋다

<br><br>