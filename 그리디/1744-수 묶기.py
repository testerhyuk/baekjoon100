"""
핵심 아이디어

- 수의 집합을 1보다 큰 수, 1, 0, 음수 이렇게 4가지 유형으로 나눠 저장한다
- 1보다 큰 수의 집합을 최댓값부터 차례대호 곱한 후 더한다. 원소의 개수가 홀 수일 때, 마지막 남은 수는 그대로 더함
- 음수의 집합을 정렬해 최솟값부터 차례대로 곱한 후 더한다. 원수의 개수가 홀 수일 때, 수열에 0이 있다면 1개 남은 음수를 0과 곱해 0을 만들고
- 수열에 0이 없다면 그대로 더한다
"""

import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
plus_pq = PriorityQueue()
minus_pq = PriorityQueue()
zero = 0
one = 0
sum = 0

for _ in range(n):
    data = int(input())

    if data > 1:
        plus_pq.put(data * -1)
    elif data < 0:
        minus_pq.put(data)
    elif data == 0:
        zero += 1
    else:
        one += 1

while plus_pq.qsize() > 1:
    data1 = plus_pq.get() * -1
    data2 = plus_pq.get() * -1
    sum += (data1 * data2)

if plus_pq.qsize() > 0:
    sum += (plus_pq.get() * -1)

while minus_pq.qsize() > 1:
    data1 = minus_pq.get()
    data2 = minus_pq.get()
    sum += (data1 * data2)

if minus_pq.qsize() > 0:
    if zero == 0:
        sum += minus_pq.get()

sum += one
print(sum)