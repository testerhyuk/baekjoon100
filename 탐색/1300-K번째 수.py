"""
핵심 아이디어

- 문제 핵심 포인트는 주어진 B의 1차원 리스트에서 k번째 인덱스에 들어갈 x가 어떤 조건을 만족해야 하는가?다
- B 리스트의 6번째라고 한다면, B[6]에는 5라는 값이 들어갈 수 있는가?, 4라는 값이 들어갈 수 있는가? 등등
- 어떤 조건으로 판별할 수 있는지 그 조건을 찾는게 핵심
- B가 오름차순으로 정렬되어야 한다고 문제에서 나와있기 때문에 만약 B[6] = 5라고 한다면
- B의 인덱스 1(시작을 1로 가정) ~ 5까지는 5보다는 작거나 같은 수가 올 수밖에 없다
- 그리고 A의 조건이 N*N 리스트이므로 k번째 수는 k를 넘지 않는다
- 따라서 조건들을 종합해보면 x 미만의 수의 개수는 k를 넘을 수 없고
- x 이하의 수의 개수는 k보다 크거나 같아야 한다
- 3X3 배열을 예로 들면
- [1, 2, 3]
- [2, 4, 6]
- [3, 6, 9]
- 이걸 B로 오름차순으로 표현하면
- [1, 2, 2, 3, 3, 4, 6, 6, 9]
- 시작을 1로 가정하고 B[7] = 6이고, 6 미만의 개수는 1, 2, 2, 3, 4로 5개
- 6 이하의 개수는 1, 2, 2, 3, 3, 4, 6, 6로 8개로 k보다 크거나 같은 값이 나온다
- 따라서, 시작 인덱스는 1, 종료 인덱스는 k로 설정해서
- 중앙값 크기보다 작은 수가 k보다 작으면 시작 인덱스 = 중앙값 + 1
- 중앙값 크기보다 작은 수가 k보다 크거나 같으면 종료 인덱스 = 중앙값 - 1로 이진 탐색을 반복
- k보다 크다가 아니라 크거나 같으면으로 설정한 이유는 k보다 크거나 같은 범위 내라면 정답 조건을 만족하는 수이기 때문에 계속 돌면서 최적의 값을 찾기 위함이다
- 시작값이 종료값보다 커지는 순간에 탐색이 종료되고 마지막에 남은 중앙값이 정답이 된다
"""

import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = k
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    # 1부터 n까지 돌면서 작은 수 찾기
    for i in range(1, n+1):
        # mid // i가 나오는 이유는 각 행이 배수의 형태를 띄고 있기 때문
        """
        [1, 2, 3] -> 1의 배수
        [2, 4, 6] -> 2의 배수
        [3, 6, 9] -> 3의 배수

        중앙값이 4라고 할 때, 4보다 작거나 같은 개수는
        1행 -> 4 // 1 -> 4개(1, 2, 3), n이 3이므로 최대값은 3이다. 따라서 n보다 큰 값은 3으로 바꿔준다
        2행 -> 4 // 2 -> 2개(2, 4)
        3행 -> 4 // 3 -> 1개(3)
        """
        cnt += min(mid//i, n)
    
    if cnt < k:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)