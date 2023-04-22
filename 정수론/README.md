# 정수론

<br><br>

| 다시 풀어볼 문제 | Tag                          | 태그                | 문제번호    | 문제이름    | 난이도    | 문제풀이    |
| :------:  | :--------------------------: | :-----------------: | :------:  | :------:  |  :------:  | :------:  |
| :heavy_check_mark: | Number Theory | 정수론 | <a href="https://www.acmicpc.net/problem/1929">1929</a> | <a href="https://www.acmicpc.net/problem/1929">소수 구하기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | [바로가기](./1929-소수%20구하기.py) |
| :heavy_check_mark: | Number Theory | 정수론 | <a href="https://www.acmicpc.net/problem/1747">1747</a> | <a href="https://www.acmicpc.net/problem/1747">소수&팰린드롬</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | [바로가기](./1747-소수&팰린드롬.py) |

<br><br>

## 소수 구하기

<br><br>

### 에라토스테네스의 체 원리

- 구하고자 하는 소수의 범위만큼 1차원 리스트 생성
- 2부터 시작하고, 현재 숫자가 지워진 상태가 아닌 경우 현재 선택된 숫자의 배수에 해당하는 수를 리스트에서 끝까지
탐색하면서 제거. 이때 처음으로 선택된 숫자는 지우지 않는다
-  리스트에 남아있는 모든 수 출력