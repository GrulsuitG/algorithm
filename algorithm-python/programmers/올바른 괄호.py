def solution(s):
    stack = 0
    for ch in s:
        if ch == '(':
            stack += 1
        elif stack:
            stack -= 1
        else:
            return False

    return stack == 0