import heapq as hq


def solution(jobs):
    total = cur = i = 0
    cnt = len(jobs)
    jobs.sort()
    heap = []

    while i < cnt:
        while jobs and cur >= jobs[0][0]:
            item = jobs.pop(0)
            hq.heappush(heap, (item[1], item[0]))

        if heap:
            (time, start) = hq.heappop(heap)
            cur += time
            total += cur - start
            i += 1
        else:
            cur = jobs[0][0]

    return total // cnt


solution([[0, 3], [4, 4], [5, 3], [4, 1]])