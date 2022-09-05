import re


def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    tmp = ''
    scores = []
    cur = 0
    for r in dartResult:
        if r.isdigit():
            cur += 1
            tmp += r
        elif r == 'S' or r == 'D' or r == 'T':
            scores.append(int(tmp) ** bonus[r])
            tmp = ''
        elif r == '*':
            scores[cur] *= 2
            if cur > 0:
                scores[cur - 1] *= 2

        elif r == '#':
            scores[cur] *= -1

    answer = sum(scores)
    return answer

def best(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
