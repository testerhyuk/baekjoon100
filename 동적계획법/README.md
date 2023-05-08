## 동적 계획법

<br><br>

| 다시 풀어볼 문제 | Tag                          | 태그                | 문제번호    | 문제이름    | 난이도    | 문제풀이    |
| :------:  | :--------------------------: | :-----------------: | :------:  | :------:  |  :------:  | :------:  |
| :heavy_check_mark: | DP | 동적 계획법 | <a href="https://www.acmicpc.net/problem/1463">1463</a> | <a href="https://www.acmicpc.net/problem/1463">1로 만들기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [바로가기](./1463-1로%20만들기.py) |
| :heavy_check_mark: | DP | 동적 계획법 | <a href="https://www.acmicpc.net/problem/14501">14501</a> | <a href="https://www.acmicpc.net/problem/14501">퇴사</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [바로가기](./14501-퇴사.py) |
| :heavy_check_mark: | DP | 동적 계획법 | <a href="https://www.acmicpc.net/problem/2193">2193</a> | <a href="https://www.acmicpc.net/problem/2193">이친수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [바로가기](./2193-이친수.py) |
| :heavy_check_mark: | DP | 동적 계획법 | <a href="https://www.acmicpc.net/problem/11726">11726</a> | <a href="https://www.acmicpc.net/problem/11726">2xn 타일링</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [바로가기](./11726-2xn%20타일링.py) |
| :heavy_check_mark: | DP | 동적 계획법 | <a href="https://www.acmicpc.net/problem/10844">10844</a> | <a href="https://www.acmicpc.net/problem/10844">쉬운 계단 수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | [바로가기](./10844-쉬운%20계단%20수.py) |

<br><br>

### 동적 계획법 핵심 원리

1. 큰 문제를 작은 문제로 나눌 수 있어야 한다
2. 작은 문제들이 반복돼 나타나고 사용되며 이 작은 문제들의 결과값은 항상 같아야 한다
3. 모든 작은 문제들은 한 번만 계산해 DP 테이블에 저장하며 추후 재사용할 때는 이 DP 테이블을 이용한다 -> 메모제이션 기법
4. 동적 계획법은 Top-Down과 Bottom-Up 방식으로 구현할 수 있다

<br><br>

### 메모이제이션

<br><br>

- 부분 문제를 풀었을 때 이 문제를 DP 테이블에 저장해 놓고 다음에 같은 문제가 나왔을 때 재계산하지 않고 DP 테이블의 값을 이용하는 것

<br><br>
<img src='https://github.com/testerhyuk/notes/blob/main/%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98.PNG?raw=true'>
<br><br>

- 위에서 2번째와 3번째 피보나치 수열은 맨 외쪽 탐색 부분에서 최초로 값이 구해지고, 이때 DP 테이블에 값이 저장된다
- 이에 따라, 나중에 2번째와 3번째 피보나치 수열의 값이 필요할 때 재연산을 이용해 구하지 않고, DP 테이블에서 바로 값을 추출한다

<br><br>

### Top-Down 방식 이해

<br><br>

- 말 그대로 위에서부터 문제를 파악해 내려오는 방식으로, 주로 재귀 함수 형태로 코드를 구현한다

<br><br>

```
import sys

input = sys.stdin.readline

n = int(input())
d = [-1] * (n+1)
d[0] = 0
d[1] = 1

def fibo(n):
    if d[n] != -1:  # 기존에 계산한 적이 있는 부분의 문제는 재계산하지 않고 리턴
        return d[n]
    
    # 메모이제이션: 구한 값을 바로 리턴하지 않고 DP 테이블에 저장한 후 리턴하도록 구현
    d[n] = fibo(n-2) + fibo(n-1)
    return d[n]

fibo(n)
print(d[n])
```

<br><br>

### Bottom-Up 방식 이해

<br><br>

- 가장 작은 부분 문제로부터 문제를 해결하면서 점점 큰 문제로 확장해 나가는 방식. 주로 반복문의 형태로 구현

<br><br>

```
import sys

input = sys.stdin.readline

n = int(input())
d = [-1] * (n+1)
d[0] = 0
d[1] = 1

for i in range(2, n+1):
    d[i] = d[i-2] + d[i-1] # 반복문을 이용해 아래서부터 값을 채워가는 방식

print(d[n])
```