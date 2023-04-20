"""
핵심 아이디어

- 데이터가 새로 삽입할 때마다 절댓값과 관련된 정렬이 필요하므로 우선순위 큐로 풀어야함
- 절댓값이 같을 때는 음수를 우선해 출력해야 한다

문제 푸는 순서

1. x = 0일 때
    - 큐가 비어 있을 떄는 0 출력, 비어 있지 않을 때는 절댓값이 최소값인 것 출력.
    - 단, 절댓값이 같다면 음수 우선 출력
2. x = 1일 때
    - put으로 큐에 새로운 값 추가하고 우선순위 큐 정렬 기준으로 자동 정렬
"""

import sys
from queue import PriorityQueue

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n = int(input())
q = PriorityQueue()

for i in range(n):
    req = int(input())
    if req == 0:
        if q.empty():
            print(0)
        else:
            # 우선수위 큐에 넣고 get()을 통해서 삭제하면 q에서 가장 작은 값이 리턴된다
            tmp = q.get()
            print(tmp[1])
    else:
        # 우선순위 큐에 데이터를 추가할 때 순서가 정렬 우선순위의 기준이 된다
        # 아래에서는 abs(req) 다음에 req를 넣었으므로 abs(req)가 정렬 우선순위의 기준이 되고
        # 첫 번째 기준이 같다면 그 다음 원소가 정렬 우선순위의 기준이 된다
        q.put((abs(req), req))
        