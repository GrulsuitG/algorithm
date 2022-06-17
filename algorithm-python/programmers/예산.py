import heapq


def solution(d, budget):
    answer = 0
    heapq.heapify(d)
    while budget > 0 and len(d):
        num = heapq.heappop(d)
        if num <= budget:
            budget -= num
            answer += 1

    return answer


def best(d, budget):
    d.sort()
    total = sum(d)
    while budget < total:
        total -= d.pop()
    return len(d)

