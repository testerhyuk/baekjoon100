import sys

input = sys.stdin.readline

n = int(input())
stack = []
res = []
op = []
cnt = 1

for i in range(1, n+1):
    p = int(input())

    while cnt <= p:
        stack.append(cnt)
        op.append('+')
        cnt += 1
    
    if stack[-1] == p:
        res.append(stack.pop())
        op.append('-')
    else:
        print('NO')
        sys.exit()
print('\n'.join(op))