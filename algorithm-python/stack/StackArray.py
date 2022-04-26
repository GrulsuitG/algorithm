# 백준 1874번
import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]


def sol():
    num = 1
    result = ''
    stack = []
    for target in arr:
        while num <= target:
            stack.append(num)
            result += '+'
            num += 1
        if stack[-1] != target:
            return 'NO'
        stack.pop()
        result += '-'

    return '\n'.join(result)

print(sol())