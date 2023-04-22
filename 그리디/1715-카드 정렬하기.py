"""
핵심 아이디어

- 작은 수부터 묶어나가야 최소 비교가 가능하다
- 가장 작은 묶음 2개를 선택해 합친다
- 합친 카드 묶음을 전체 카드 묶음에 넣고 다시 오름차순으로 정렬한다
- 삽입, 삭제, 정렬이 반복되므로 우선순위 큐를 써서 풀 수 있다
"""

import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    # put 메서드로 원소를 집어넣으면 Priority Queue에서 자동 정렬한다
    pq.put(int(input()))

data1 = 0
data2 = 0
sum = 0

while pq.qsize() > 1:
    # Priority Queue에서 get은 맨 앞에 원소를 삭제한다
    data1 = pq.get()
    data2 = pq.get()
    temp = data1 + data2
    sum += temp
    pq.put(temp)

print(sum)