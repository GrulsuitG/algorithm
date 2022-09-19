from collections import defaultdict


def solution(survey, choices):
    answer = ''
    score = defaultdict(int)
    for s, choice in zip(survey, choices):
        if choice > 4:
            score[s[1]] += choice - 4
        else:
            score[s[0]] += 4 - choice

    for char in ["RT", "CF", "JM", "AN"]:
        if char[0] < char[1]:
            answer += char[1]
        else:
            answer += char[0]

    return answer

solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])