# 백준 13305번
import sys

N = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))[:-1]

total = 0
cur = 0
minimum = min(price)

while True:
    if price[cur] == minimum:
        total += sum(length[cur:]) * price[cur]
        break
    else:
        for i in range(cur, N-1):
            if price[cur] <= price[i]:
                total += price[cur] * length[i]
            else:
                cur = i
                break

print(total)

