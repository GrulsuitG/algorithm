import math
from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    items = set(map(int, numbers))
    for i in range(2, len(numbers) + 1):
        for item in list(permutations(numbers, i)):
            items.add(int(''.join(item)))

    m = max(items)
    prime = [True] * (m + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(math.sqrt(m)) + 1):
        if prime[i]:
            j = 2
            while i * j <= m:
                prime[i *j] = False
                j += 1

    for item in items:
        if prime[int(item)]:
            answer += 1

    return answer

def best(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
