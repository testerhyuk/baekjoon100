## 조합

<br><br>

| 다시 풀어볼 문제 | Tag                          | 태그                | 문제번호    | 문제이름    | 난이도    | 문제풀이    |
| :------:  | :--------------------------: | :-----------------: | :------:  | :------:  |  :------:  | :------:  |
| :heavy_check_mark: | Combination | 조합 | <a href="https://www.acmicpc.net/problem/11050">11050</a> | <a href="https://www.acmicpc.net/problem/11050">이항 계수 1</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/5.svg"/> | [바로가기](./11050-이항%20계수%201.py) |
|  | Combination | 조합 | <a href="https://www.acmicpc.net/problem/11051">11051</a> | <a href="https://www.acmicpc.net/problem/11051">이항 계수 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | [바로가기](./11051-이항%20계수%202.py) |
| :heavy_check_mark: | Combination | 조합 | <a href="https://www.acmicpc.net/problem/2775">2775</a> | <a href="https://www.acmicpc.net/problem/2775">부녀회장이 될테야</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/5.svg"/> | [바로가기](./2775-부녀회장이%20될테야.py) |
| :heavy_check_mark: | Combination | 조합 | <a href="https://www.acmicpc.net/problem/1010">1010</a> | <a href="https://www.acmicpc.net/problem/1010">다리 놓기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | [바로가기](./1010-다리%20놓기.py) |
| :heavy_check_mark: | Combination | 조합 | <a href="https://www.acmicpc.net/problem/1256">1256</a> | <a href="https://www.acmicpc.net/problem/1256">사전</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> | [바로가기](./1256-사전.py) |
| :heavy_check_mark: | Combination | 조합 | <a href="https://www.acmicpc.net/problem/1947">1947</a> | <a href="https://www.acmicpc.net/problem/1947">선물 전달</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> | [바로가기](./1947-선물%20전달.py) |

<br><br>

### 순열 조합 핵심 이론

- 조합 : n개의 숫자에서 r개를 뽑는 경우의 수
- 순열 : n개의 숫자 중 r개를 뽑아 순서를 고려해 나열할 경우의 수
- 조합이 코딩테스트에서 많이 쓰이며 동적계획법의 시작이다
- 알고리즘에서는 조합의 수학 공식을 코드화하지 않고 점화식을 사용해서 표현한다

### 점화식 세우기

1. 특정 문제를 가정하기
    - 예를 들어, 5개의 데이터에서 3개를 선택하는 조합의 경우의 수

    <br><br>
    <img src='https://github.com/testerhyuk/notes/blob/main/%EC%A1%B0%ED%95%A91.PNG?raw=true'>
    <br><br>

2. 모든 부분 문제가 해결된 상황이라고 가정하고 지금 문제 생각하기
    - 먼저 5개의 데이터 중 4개가 이미 선택 여부가 결정된 데이터라고 가정한다
    - 그리고 5번째 데이터의 선택 여부에 따른 경우의 수를 계산한다
    - 만약 5번째 데이터를 포함해 총 3개의 데이터를 선택하려면 선택이 완료됐다고 가정한 4개의 데이터에서 2개가 선택되어 있어야 한다
    - 5번째 데이터를 포함하지 않고 총 3개의 데이터를 선택하려면 이전 데이터 4개 중 3개가 선택되어 있어야 한다
    - 이 2가지 경우의 수를 합치면 데이터 5개 중 3개를 선택하는 경우의 수가 나온다

    <br><br>
    <img src='https://github.com/testerhyuk/notes/blob/main/%EC%A1%B0%ED%95%A92.PNG?raw=true'>
    <br><br>

3. 5개 중 3개를 선택하는 경우의 수 점화식
    - D[5][3] = D[4][2] + D[4][3]
    - 결국 D[i][j] = D[i-1][j] + D[i-1][j-1]이 된다