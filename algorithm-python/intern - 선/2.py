def solution(n, times):
    MAX = 987654321
    dp = [MAX] * (n + 1)
    dp[2] = times[0]
    for i in range(3, n + 1):
        # 1개만 잘라서 추가하는 경우

        for j in range(min(i//2, len(times))):
            dp[i] = min(dp[i], dp[i - 1 - j] + times[j])

    return dp[n]


print(solution(5, [2, 4, 5]))