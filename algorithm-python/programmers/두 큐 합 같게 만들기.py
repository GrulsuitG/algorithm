def solution(queue1, queue2):
    answer = 0
    if sum(queue1) > sum(queue2):
        queue1, queue2 = queue2, queue1

    queSum = (sum(queue1) + sum(queue2))
    if queSum % 2:
        return -1
    target = queSum // 2

    start, end = 0, len(queue1)
    cur = sum(queue1)
    queue3 = queue1 + queue2

    while end < len(queue3):
        if cur == target:
            break
        elif cur < target:
            cur += queue3[end]
            end += 1
        else:
            cur -= queue3[start]
            start += 1
        answer += 1
    if end == len(queue3) and cur != target:
        answer = -1
    return answer

solution([3, 2, 7, 2], [4, 6, 5, 1])
