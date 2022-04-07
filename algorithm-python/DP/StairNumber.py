# 백준 10844

N = int(input())

memo = [[1] * 10]
memo[0][0] = 0
for i in range(1, N):
    temp = [0] * 10
    for num in range(0, 10):
        if num == 0:
            temp[1] += memo[i-1][0]
        elif num == 9:
            temp[8] += memo[i-1][9]
        else:
            temp[num + 1] += memo[i-1][num]
            temp[num - 1] += memo[i-1][num]
    memo.append(temp)


print(sum(memo[N-1]) % 1000000000)
