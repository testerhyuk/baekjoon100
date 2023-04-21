import sys

input = sys.stdin.readline

n = int(input())

# 소수 판별 함수
def isPrime(p):
    # 소수를 판별할 때는 전부 돌 필요 없고 기준 값에 반만 돌면 찾을 수 있다
    for i in range(2, p//2 + 1):
        if p%i == 0:
            return False
    return True

def dfs(v):
    # 첫 번째 파라미터를 제외한 나머지 수는 전부 소수만 파라미터로 들어오므로
    # 여기서 4 자리수만 판별해서 4자리수라면 출력해주면 된다
    if len(str(v)) == n:
        print(v)
    else:
        # 자리수 늘리는건 재귀로 늘려주므로
        # 일의 자리만 업데이트 할 수 있도록 for문을 돈다
        for i in range(1, 10):
            # 2의 배수는 결국 소수가 아니므로 제외
            if i%2 == 0:
                continue
            # 들어온 값의 자리수를 소수 판별 함수로 넘김
            if isPrime(v*10 + i):
                # 소수라면 재귀로 자리수를 늘림
                dfs(v*10 + i)

# 2, 3, 5, 7만 넘겨준 이유는
# 일의 자리에서 2, 3, 5, 7만 소수이기 때문
dfs(2)
dfs(3)
dfs(5)
dfs(7)