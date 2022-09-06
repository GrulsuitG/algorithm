from collections import deque


def solution(cacheSize, cities):
    answer = 0
    queue = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in queue:
            answer += 1
            queue.remove(city)
            queue.append(city)
        else:
            answer += 5
            queue.append(city)

    return answer
