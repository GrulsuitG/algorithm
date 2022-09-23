import heapq


def solution(stones, k):
    answer = 0

    heap = list((stones[idx], idx) for idx in range(len(stones)))
    heapq.heapify(heap)
    while heap and heap[0][0] >= answer:
        stone = heapq.heappop(heap)

        if stone[0] == answer:
            continue

        lo = max(stone[1] - k, 0)
        hi = min(stone[1] + k, len(stones))

        cnt = 0
        for i in range(stone[1] - 1, lo - 1, -1):
            if stones[i] > answer:
                break
            else:
                cnt += 1
        if cnt == k:
            break
        cnt = 0

        for j in range(stone[1] + 1, hi + 1):
            if stones[j] > answer:
                break
            else:
                cnt += 1

        if cnt == k:
            break
        answer = stone[0]

    return answer


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)