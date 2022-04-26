# 백준 4949번
import sys

result = []
while True:
    line = sys.stdin.readline()
    if line == '.\n':
        break

    stack = []
    for c in line:
        if c == '(':
            stack.append('(')
        elif c == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append('-1')
                break
        elif c == '[':
            stack.append('[')
        elif c == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append('-1')
                break

    if len(stack) == 0:
        result.append('yes')
    else:
        result.append('no')

print('\n'.join(result))