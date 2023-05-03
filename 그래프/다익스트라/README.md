## 다익스트라

<br><br>

- 그래프에서 최단 거리를 구하는 알고리즘
- BFS와의 차이점으로는 다익스트라는 보통 가중치가 있는 그래프에서의 최단 거리를 구할 때 쓴다

<br><br>

### 다익스트라 핵심 이론

<br><br>

1. 인접 리스트로 그래프 구현

<br><br>
<img src='https://github.com/testerhyuk/notes/blob/main/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC1.PNG?raw=true'>
<br><br>

2. 최단 거리 리스트 초기화
    - 출발 노드는 0, 이외의 노드는 무한으로 초기화 한다
    - 무한은 적당히 큰 값을 사용하면 된다

<br><br>
<img src='https://github.com/testerhyuk/notes/blob/main/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC2.PNG?raw=true'>
<br><br>

3. 값이 가장 작은 노드 고르기
    - 최단 거리 리스트에서 현재 값이 가장 작은 노드를 고른다

<br><br>
<img src='https://github.com/testerhyuk/notes/blob/main/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC3.PNG?raw=true'>
<br><br>

4. 최단 거리 리스트 업데이트
    - 선택된 노드에 연결된 에지의 값을 바탕으로 다른 노드의 값을 업데이트한다
    - 연결 리스트를 이용해 현재 선택된 노드에 이지들을 탐색하고 업데이트하면 된다
    - 연결 노드의 최단 거리는 두 값 중 더 작은 값으로 업데이트한다
    - min(선택 노드의 최단 거리 리스트의 값 + 에지 가중치, 연결 노드의 최단 거리 리스트의 값)

<br><br>
<img src='https://github.com/testerhyuk/notes/blob/main/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC4.PNG?raw=true'>
<br><br>

5. 과정 3~4를 반복해 최단 거리 리스트 완성

<br><br>
<img src='https://github.com/testerhyuk/notes/blob/main/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC5.PNG?raw=true'>