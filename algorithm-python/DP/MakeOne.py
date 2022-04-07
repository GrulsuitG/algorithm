# 백준 1463번

N = int(input())

# 처음 짠 코드 Brute Force 로 1 ~ N 까지 다 계산 Bottom - Up
# memo = [0, 0, 1, 1]
#
# for i in range(4, N + 1):
#     result = []
#     if i % 3 == 0:
#         result.append(memo[i // 3] + 1)
#     if i % 2 == 0:
#         result.append(memo[i // 2] + 1)
#
#     result.append(memo[i - 1] + 1)
#
#     memo.append(min(result))
#
# print(memo[N])

# 두번째 짠 코드 BFS 로 필요한 것만 계산 Top - Down
group = set()
group.add(N)
time = 0
while 1 not in group:
    time += 1
    temp = set()
    for i in group:
        if i % 3 == 0:
            temp.add(i//3)
        if i % 2 == 0:
            temp.add(i//2)
        temp.add(i-1)
    group = temp

print(time)