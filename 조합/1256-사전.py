import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

d = [[0 for _ in range(202)] for _ in range(202)]

answer = ''

for i in range(201):
    for j in range(i+1):
        if j == 0 or j == i:
            d[i][j] = 1
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j]
            if d[i][j] > 1000000000:
                d[i][j] = 1000000000

if d[n+m][m] < k:
    print(-1)
else:
    while not (n==0 and m==0):
        split = d[n-1+m][m]

        if k <= split:
            n -= 1
            answer += 'a'
        else:
            m -= 1
            k -= split
            answer += 'z'

print(answer)