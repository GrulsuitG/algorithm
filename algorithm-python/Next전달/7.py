def solution(money, stocks):
    dp = [0] * (money + 1)

    for stock in stocks:
        for i in range(1, money + 1):
            if stock[1] <= i:
                dp[i] = dp[i - stock[0]] + stock[1]
                break

    return max(dp)





solution(10, [[1, 1], [3, 5], [3, 5], [4, 9]])