from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_weights = deque(truck_weights)
    crossing = deque(0 for i in range(bridge_length - 1))
    crossing.appendleft(truck_weights.popleft())
    total_weight = sum(crossing)
    while crossing:
        total_weight -= crossing.pop()
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                total_weight += truck_weights[0]
                crossing.appendleft(truck_weights.popleft())

            else:
                crossing.appendleft(0)

        answer += 1

    return answer