# 백준 9012번
import sys

N = int(sys.stdin.readline())

result = []
for i in range(N):
    stack = []
    s = sys.stdin.readline()
    flag = False
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                flag = True
                break

    if len(stack) == 0 and flag is False:
        result.append('YES')
    elif len(stack) != 0 or flag:
        result.append('NO')



print('\n'.join(result))