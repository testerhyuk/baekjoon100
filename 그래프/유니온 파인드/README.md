## 유니온 파인드

<br><br>

### 핵심 이론

<br><br>

- 여러 노드가 있을 때 특정 2개의 노드를 연결해 1개의 집합으로 묶는 union 연산과 두 노드가 같은 집합에 속해 있는지를 확인하는 find 연산으로 구성
- union 연산 : 각 노드가 속한 집합을 1개로 합치는 연산
- find 연산 : 특정 노드 a에 관해 a가 속한 집한의 대표 노드를 반환하는 연산

<br><br>

#### 구현 방법

<br><br>

1. 1차원 리스트를 이용한다
    - 처음에는 노드가 연결되어 있지 않으므로 각 노드가 대표 노드가 된다
    - 각 노드가 모두 대표 노드이므로 리스트는 자신의 인덱스값으로 초기화한다

    <br><br>
    <img src='https://github.com/testerhyuk/notes/blob/main/%EC%9C%A0%EB%8B%88%EC%98%A8%ED%8C%8C%EC%9D%B8%EB%93%9C1.PNG?raw=true'>
    <br><br>

2. 2개의 노드를 선택해 각각의 대표 노드를 찾아 연결하는 union 연산을 수행
    - 리스트를 보면 1, 4와 5, 6을 union 연산으로 연결한다
    - 리스트[4]는 1로, 리스트[6]은 5로 업데이트한다
    - 1은 대표 노드, 4는 자식노드로 union 연산을 하므로 리스트[4]의 대표 노드를 1로 설정한 것이다
    - 그 결과 각각의 집합이었던 1, 4는 하나로 합쳐진다
    - 5, 6도 마찬가지
    - 대표 노드는 보통 작은 인덱스 쪽으로 설정한다

    <br><br>
    <img src='https://github.com/testerhyuk/notes/blob/main/%EC%9C%A0%EB%8B%88%EC%98%A8%ED%8C%8C%EC%9D%B8%EB%93%9C2.PNG?raw=true'>
    <br><br>

3. find 연산을 통해 자신이 속한 집합의 대표 노드를 찾는다
    - 4와 6을 연결해보자
    - 4와 6은 모두 대표 노드가 아니다. 따라서 각 노드의 대표 노드를 찾아 올라간 다음 그 대표 노드를 연결한다
    - 4의 대표 노드는 1, 6의 대표 노드는 5이므로 1과 5를 연결한다
    - 대표 노드는 보통 작은 인덱스 쪽으로 설정하므로 인덱스 5의 값이 1로 바뀐다

    <br><br>
    <img src='https://github.com/testerhyuk/notes/blob/main/%EC%9C%A0%EB%8B%88%EC%98%A8%ED%8C%8C%EC%9D%B8%EB%93%9C3.PNG?raw=true'>
    <br><br>

###### find 연산 작동 원리

<br><br>

1. 대상 노드 리스트에 index값과 value값이 동일한지 확인한다
2. 동일하지 않으면 value값이 가리키는 index 위치로 이동
3. 이동 위치의 index값과 value값이 같을 때까지 1번과 2번을 반복한다. 반복은 재귀로 구현
4. 대표 노드에 도달하면 재귀 함수를 빠져나오면서 거치는 모든 노드값을 대표 노드값으로 변경한다

<br><br>
<img src='https://github.com/testerhyuk/notes/blob/main/find%EC%9B%90%EB%A6%AC.PNG?raw=true'>