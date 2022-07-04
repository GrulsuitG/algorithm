def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for h in range(1, n + 1):
        if citations[n - h] >= h:
            answer = h
    return answer