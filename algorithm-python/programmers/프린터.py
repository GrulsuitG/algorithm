def solution(priorities, location):
    answer = 0
    while priorities:
        item = priorities.pop(0)
        if len(priorities) == 0:
            answer += 1
            break
        else:
            if item < max(priorities):
                priorities.append(item)
            else:
                answer += 1
                if location == 0:
                    break

        if location == 0:
            location = len(priorities) - 1
        else:
            location -= 1
    return answer


def best(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
