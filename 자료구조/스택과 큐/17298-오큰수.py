"""
핵심 아이디어

1. 스택에 새로 들어오는 수가 top에 존재하는 수보다 크면 오큰수
2. 오큰수를 구하고 수열에서 오큰수가 존재하지 않는 숫자에 -1 출력

문제 푸는 순서

1. 스택이 채워져 있거나 A[index] > A[top]인 경우 pop한 인덱스를 이용해 정답 수열에 오큰수 저장
2. pop은 조건을 만족하는 동안 반복
3. 현재 인덱스를 스택에 push하고 다음 인덱스로 넘어간다
4. 스택에 남아있는 인덱스에 -1을 저장
"""

import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

n = int(input())
nge = list(map(int, input().split()))
stack = []
ans = [0] * n

for i in range(n):
    while stack and nge[stack[-1]] < nge[i]:
        ans[stack.pop()] = nge[i]
    stack.append(i)

# for문 돌고 나왔는데 stack이 비어있지 않는 경우 -1 넣기
while stack:
    ans[stack.pop()] = -1

for i in ans:
    print(i, end=' ')