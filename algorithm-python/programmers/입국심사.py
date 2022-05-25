def solution(n, times):
    l = 0
    r = max(times) * n
    while l <= r:
        m = (l + r) // 2
        cnt = 0
        for time in times:
            cnt += m // time
        if cnt >= n:
            r = m - 1
        else:
            l = m + 1

    return l