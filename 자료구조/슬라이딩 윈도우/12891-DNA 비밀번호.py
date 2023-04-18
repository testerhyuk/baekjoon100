"""
핵심 아이디어

1. 범위 p만큼의 문자열을 확인하면서 체크리스트 업데이트
2. 체크했으면 오른쪽으로 1칸 이동
3. 빠지는 문자열의 개수 제거하고 새로 들어오는 문자열의 개수 업데이트
"""

import sys

input = sys.stdin.readline

s, p = map(int, input().split())
dna = list(input().rstrip())
n = list(map(int, input().split()))
check = [0] * 4 # 내가 채워나갈 체크 리스트
equal = 0
cnt = 0

for i in n:
    if i == 0:
        equal += 1

def addCheck(c):
    global equal

    if c == 'A':
        check[0] += 1
        # 내가 체크한 값과 주어진 최소 값이 일치하면 equal 증가
        # == 을 쓴 이유는 한 번만 증가시켜주기 위해
        if check[0] == n[0]:
            equal += 1
    elif c == 'C':
        check[1] += 1
        if check[1] == n[1]:
            equal += 1
    elif c == 'G':
        check[2] += 1
        if check[2] == n[2]:
            equal += 1
    else:
        check[3] += 1
        if check[3] == n[3]:
            equal += 1

def delCheck(c):
    global equal

    if c == 'A':
        # 값이 같다면 equal 감소
        # ==을 쓴 이유는, 만약에 check[0]이 이미 최소값을 만족하지 못한다면(n[0]보다 작다면)
        # delCheck 하기전 addcheck에서 이미 만족하지 못해 equal이 증가하지 않았을 것이다
        # 따라서 == 만으로도 조건이 충족된다 
        if check[0] == n[0]:
            equal -= 1
        check[0] -= 1
    elif c == 'C':
        if check[1] == n[1]:
            equal -= 1
        check[1] -= 1
    elif c == 'G':
        if check[2] == n[2]:
            equal -= 1
        check[2] -= 1
    else:
        if check[3] == n[3]:
            equal -= 1
        check[3] -= 1

# 첫번째 범위만 체크한다
for i in range(p):
    addCheck(dna[i])

if equal == 4:
    cnt += 1

# 첫번째 범위 체크 후 p부터 1씩 증가하면서
# p(새로 들어가는 문자)를 체크하고
# j(빠져야할 문자)를 체크한다
for i in range(p, s):
    j = i - p
    addCheck(dna[i])
    delCheck(dna[j])

    if equal == 4:
        cnt += 1

print(cnt)