answer = 0
visit = []


def solution(k, dungeons):
    global visit
    visit = [False] * len(dungeons)
    dfs(k, 0, dungeons)
    return answer


def dfs(k, time, dungeons):
    global answer
    answer = max(answer, time)
    for idx, dungeon in enumerate(dungeons):
        if not visit[idx] and k >= dungeon[0]:
            visit[idx] = True
            dfs(k - dungeon[1], time + 1, dungeons)
            visit[idx] = False


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
