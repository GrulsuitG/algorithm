from collections import defaultdict


def solution(clothes):
    answer = 1
    kinds = defaultdict(list)
    for cloth in clothes:
        kinds[cloth[1]].append(cloth[0])

    for kind in kinds:
        answer *= len(kinds[kind]) + 1
    return answer - 1

