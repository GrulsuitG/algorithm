import heapq as hq


def solution(operations):
    heap = []

    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            hq.heappush(heap, int(num))

        elif op == 'D':
            if len(heap) == 0:
                continue
            elif num == '1':
                heap = hq.nlargest(len(heap), heap)[1:]
                hq.heapify(heap)
            else:
                hq.heappop(heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), heap[0]]

    return answer