import math


def solution(progresses, speeds):
    answer = [1]

    cur = round((100 - progresses[0]) / speeds[0])
    idx = 0
    for i in range(1, len(progresses)):
        day = ((100 - progresses[i]) / speeds[i])
        if day <= cur:
            answer[idx] += 1
        else:
            answer.append(1)
            cur = day
            idx += 1

    return answer

solution([1, 1, 1], [100, 94, 95])


print(math.ceil((100 - 1) / 94))