# 백준 10866번
import sys

N = int(sys.stdin.readline())

stack = []
front = 0
back = 0
result = []
for _ in range(N):
    args = sys.stdin.readline().split()
    if args[0] == 'push_front':
        stack.insert(front, str(args[1]))
        back += 1
    elif args[0] == 'push_back':
        stack.append(str(args[1]))
        back += 1
    elif args[0] == 'pop_front':
        if front == back:
            result.append('-1')
        else:
            result.append(str(stack[front]))
            front += 1
    elif args[0] == 'pop_back':
        if front == back:
            result.append('-1')
        else:
            result.append(str(stack.pop()))
            back -= 1
    elif args[0] == 'size':
        result.append(str(back - front))
    elif args[0] == 'empty':
        if back == front:
            result.append('1')
        else:
            result.append('0')
    elif args[0] == 'front':
        if back == front:
            result.append('-1')
        else:
            result.append(str(stack[front]))
    elif args[0] == 'back':
        if back == front:
            result.append('-1')
        else:
            result.append(str(stack[back-1]))

print('\n'.join(result))
