# 백준 17298번
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

stack = [0]
result = [-1] * N
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(' '.join(map(str, result)))
