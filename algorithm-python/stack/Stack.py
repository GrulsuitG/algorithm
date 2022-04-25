# 백준 10828번
import sys

N = int(sys.stdin.readline())

stack = []
num = 0
result = []
for _ in range(N):
    args = sys.stdin.readline().split()
    if args[0] == 'push':
        stack.append(str(args[1]))
        num += 1
    elif args[0] == 'pop':
        if num == 0:
            result.append('-1')
        else:
            result.append(str(stack[num-1]))
            stack.pop(num-1)
            num -= 1
    elif args[0] == 'size':
        result.append(str(num))
    elif args[0] == 'empty':
        if num == 0:
            result.append('1')
        else:
            result.append('0')
    elif args[0] == 'top':
        if num == 0:
            result.append('-1')
        else:
            result.append(str(stack[num-1]))

print('\n'.join(result))

