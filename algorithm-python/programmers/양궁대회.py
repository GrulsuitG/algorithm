maxScore = 0
answer = []


def solution(n, info):
    global answer, maxScore
    dfs(n, info, [0] * 11, 0)

    if maxScore == 0:
        return [-1]
    else:
        answer = sorted(answer)
        print(answer)
        return answer[-1]


def dfs(n, apeachs, lions, cur):
    if cur == 11:
        return calcScore(lions, apeachs)

    target = apeachs[cur] + 1

    if target <= n:
        lions[cur] = target
        dfs(n - target, apeachs, lions, cur + 1)
        lions[cur] = 0

    return dfs(n, apeachs, lions, cur + 1)


def calcScore(lions, apeachs):
    global maxScore, answer

    score = 0
    lions[-1] = sum(apeachs) - sum(lions)
    for idx, (lion, apeach) in enumerate(zip(lions, apeachs)):
        if lion > apeach:
            score += 10 - idx
        elif apeach != 0:
            score -= 10 - idx

    if maxScore < score:
        maxScore = score
        answer = [[i for i in lions]]
    elif maxScore == score:
        answer.append([i for i in lions])
    lions[-1] = 0
    return score


solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])