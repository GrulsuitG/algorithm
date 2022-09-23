def solution(s):
    answer = -1
    for i in range(10):
        sub = str(i) * 3
        if sub in s:
            answer = int(sub)
    return answer

print(solution("111999333"))