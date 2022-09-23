import heapq


def solution(n, t, m, timetable):
    start = 540
    table = []
    l = []
    for times in timetable:
        _h, _m = times.split(':')
        heapq.heappush(table, int(_h) * 60 + int(_m))

    last_bus = start + (n - 1) * t
    for cur_time in range(start, last_bus + 1, t):
        cnt = 0
        while cnt < m:
            if table:
                if table[0] <= cur_time:
                    last = heapq.heappop(table)
                    cnt += 1
                else:
                    break
            else:
                break

    if cnt == m:
        _h, _m = (last - 1) // 60, (last - 1) % 60
    else:
        _h, _m = last_bus // 60, last_bus % 60

    if _h < 10:
        _h = '0' + str(_h)
    if _m < 10:
        _m = '0' + str(_m)

    return str(_h) + ':' + str(_m)