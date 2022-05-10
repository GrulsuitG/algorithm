# 백준 1300번

N = int(input())
k = int(input())

s = 1
e = k

while s <= e:
    m = (s + e) // 2

    cnt = 0
    for i in range(1, N+1):
        cnt += min(m // i, N)

    if cnt >= k:
        e = m - 1
    elif cnt < k:
        s = m + 1

print(s)

