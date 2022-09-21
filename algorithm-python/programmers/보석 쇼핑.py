from collections import Counter


def solution(gems):
    answer = [1, len(gems)]
    target = len(set(gems))
    start, end = 0, 0
    shop = Counter()
    while start <= end:
        if len(set(shop)) == target:
            if answer[1] - answer[0] > end - (start + 1):
                answer = [start + 1, end]
            elif answer[1] - answer[0] == end - (start + 1) and start + 1 < answer[0]:
                answer = [start + 1, end]
            shop[gems[start]] -= 1
            if shop[gems[start]] == 0:
                del shop[gems[start]]
            start += 1

        elif end < len(gems):
            shop[gems[end]] += 1
            end += 1
        else:
            start += 1
    return answer


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])