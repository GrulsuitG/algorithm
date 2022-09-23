from pprint import pprint


def solution(n, s, a, b, fares):
    MAX = 9999999999
    prices = [[0 if i == j else MAX for i in range(n + 1)] for j in range(n + 1)]

    for c, d, f in fares:
        prices[c][d] = f
        prices[d][c] = f

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                prices[j][k] = min(prices[j][k], prices[j][i] + prices[i][k])

    pprint(prices)

    return min(prices[s][i] + prices[i][a] + prices[i][b] for i in range(1, n+1))


solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])