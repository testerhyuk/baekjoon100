## 위상 정렬

<br><br>

- 위상 정렬은 사이클이 없는 방향 그래프에서 노드 순서를 찾는 알고리즘이다
- 반드시 사이클이 없어야 위상 정렬 알고리즘을 사용할 수 있다
- 위상 정렬이 늘 같은 정렬 결과를 보장하지 않는다

<br><br>

#### 핵심 원리

<br><br>

1. 진입 차수 리스트 업데이트
    - 진입 차수란 자기 자신을 가리키는 에지의 개수

    <br><br>
    <img src='https://github.com/testerhyuk/notes/blob/main/%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC1.PNG?raw=true'>
    <br><br>

2. 진입 차수 리스트에서 진입 차수 0인 노드 선택 후 정렬 리스트에 저장한다.
3. 이후 인접 리스트에서 선택된 노드가 가리키는 노드들의 진입 차수를 1씩 뺀다

    <br><br>
    <img src='https://github.com/testerhyuk/notes/blob/main/%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC2.PNG?raw=true'>
    <img src='https://github.com/testerhyuk/notes/blob/main/%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC3.PNG?raw=true'>