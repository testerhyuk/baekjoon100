"""
핵심 아이디어

- "크기가 같고 순서가 바뀌지 않아야함"이 이진 탐색 알고리즘을 선택하게 하는 실마리
- 첫 레슨부터 마지막 레슨까지 차례대로 저장해보고 모두 저장할 수 있다면 크기를 줄이고 저장할 수 없다면 크기를 늘린다
- 이 방식으로 블루레이 크기의 최솟값을 알 수 있다
- 이진 탐색의 시작 인덱스는 최대 길이의 레슨
- 이진 탐색의 종료 인덱스는 모든 레슨 길이의 합이다
- 이 문제에서는 시작 인덱스는 9, 종료 인덱스는 1~9의 합인 45가 된다
- 이진탐색을 하면서 중앙값 크기로 모든 레슨을 저장할 수 있다면 종료 인덱스 = 중앙값 - 1
- 저장할 수 없다면 시작 인덱스 = 중앙값 + 1
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lecture = list(map(int, input().split()))

start = max(lecture)
end = 0

for i in lecture:
    end += i

while start <= end:
    mid = (start + end) // 2
    sum = 0
    cnt = 0

    # 중간 값으로 모든 레슨을 저장할 수 있는지 확인
    for i in range(n):
        if sum + lecture[i] > mid:
            cnt += 1
            sum = 0
        sum += lecture[i]
    
    # 레슨을 모두 저장해도 중간값보다 작은 경우
    # 또는, 앞에부터 저장하고 다음 블루레이로 넘어가서 저장했는데 중간값보다 작은 경우
    # 이 때 중간값보다 작더라도 추가 블루레이가 필요하므로 cnt 증가
    if sum != 0:
        cnt += 1

    # 블루레이의 개수가 정해진 개수보다 크다는 말은 중간값이 작다는 의미
    if cnt > m:
        start = mid + 1
    # 반대로 중간값이 크다는 의미
    else:
        end = mid - 1

# while문에서 cnt랑 m값이 같아도 멈추지 않고 진행하게 두는데
# 현재 상태보다 더 효율적인 값이 있는지 계속 체크해나가기 위함
# 없더라도 start랑 end가 늘고 줄어가면서 결국 시작 인덱스가 정답으로 수렴하게됨
print(start)