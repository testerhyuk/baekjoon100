import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1) # 대표 노드 리스트 초기화

for i in range(0, n+1):
    parent[i] = i
           
def find(a):  # find 연산
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 재귀 함수로 대표 노드 찾아가기
        return parent[a]

def union(a, b): # 대표 노드끼리 합치기
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

def checkSame(a, b): # 두 원소가 같은 집합에 속해있는지 체크
    a = find(a)
    b = find(b)

    if a == b:
        return True
    else:
        return False

for i in range(m):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print('YES')
        else:
            print('NO')