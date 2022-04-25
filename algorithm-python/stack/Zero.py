# 백준 10773번
import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    m = int(sys.stdin.readline())

    if m == 0:
        stack.pop()
    else:
        stack.append(m)

print(sum(stack))
