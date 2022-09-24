import heapq


def solution(fuel, powers, distances):
    answer = 0
    n = len(powers)
    times = []
    distribute = [1] * n

    for i in range(n):
        times.append([-get_time(1, powers[i], distances[i]), i])
    heapq.heapify(times)

    total = n
    while total < fuel:
        _, idx = heapq.heappop(times)
        distribute[idx] += 1
        time = -get_time(distribute[idx], powers[idx], distances[idx])
        cnt = 1
        while time < times[0][0]:
            distribute[idx] += 1
            time = -get_time(distribute[idx], powers[idx], distances[idx])
            cnt += 1
        total += cnt
        heapq.heappush(times, [time, idx])

    answer = int(-times[0][0])
    answer = answer if answer == -times[0][0] else answer + 1
    return answer

def get_time(f, p, d):
    return d / (f * p) + f / 2


solution(8, [20, 30], [750, 675])