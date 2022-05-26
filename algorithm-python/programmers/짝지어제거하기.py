def solution(s):
    stack = []

    for c in s:
        stack.append(c)
        while len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    return 0 if len(stack) else 1


def best(s):
    stack = []
    for c in s:
        if len(stack) and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return 0 if len(stack) else 1
