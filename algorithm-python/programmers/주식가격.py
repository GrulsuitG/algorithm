from collections import deque


def solution(prices):
    answer = [0] * len(prices)
    prices = deque(prices)
    time = 1
    stack = [(prices.popleft(), 0)]
    for i in range(1, len(prices)):
        while stack and stack[-1][0] > prices[0]:
            _, idx = stack.pop()
            answer[idx] = time - idx

        stack.append((prices.popleft(), i))
        time += 1
    while stack:
        _, idx = stack.pop()
        answer[idx] = time - idx

    return answer