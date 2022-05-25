def solution(N, number):
    dp = [[-1]]
    dp.append([N])
    dp.append([int(str(N) * 2), 1, N * N, N + N])

    for i in range(3, 9):
        dp.append(set())
        for j in range(1, i // 2 + 1):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a * b)
                    if b - a > 0:
                        dp[i].add(b - a)
                    if b // a != 0:
                        dp[i].add(b // a)

    for i in range(1, 9):
        if number in dp[i]:
            return i

    return -1

print(solution(5, 12))