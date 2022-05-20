def solution(s):
    answer = 987654321
    str_len = len(s)
    if str_len == 1:
        return 1
    for i in range(1, str_len // 2 + 1):
        cur = 0
        stack = []
        compression = ''
        while cur <= str_len:
            target = s[cur:cur+i]
            if len(stack) == 0:
                stack.append(target)
                cur += i
            elif stack[-1] == target:
                stack.append(target)
                cur += i
            else:
                if len(stack) == 1:
                    compression += stack[-1]
                else:
                    compression += str(len(stack)) + stack[-1]
                stack = []
        for word in stack:
            compression += word
        answer = min(answer, len(compression))
    return answer

print(solution('a'))