import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
psum = [0] * (n+1)  # 합 배열을 n+1개로 초기화

for i in range(1, n+1):
    # 합 배열을 n+1로 초기화했기 때문에 psum[i-1]에서 오류가 발생하지 않음
    psum[i] = psum[i-1] + lst[i-1]

for _ in range(m):
    s, e = map(int, input().split())
    """
    리스트 A =  [5, 4, 3, 2, 1]
    합 배열 S = [5, 9, 12, 14, 15]
    특정 구간의 합은 S[end] - S[start-1]

    start = 1, end = 3일 때
    1에서 3구간의 합은
    A[1] + A[2] + A[3]
    
    합 배열에서 보면 
    S[3] - S[0]이고 이걸 풀어보면
    A[0] + A[1] + A[2] + A[3] - A[0] = A[1] + A[2] + A[3]
    """
    print(psum[e] - psum[s-1])