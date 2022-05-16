from itertools import combinations
import math


def solution(nums):
    answer = 0

    for comb in combinations(nums, 3):
        num = sum(comb)
        if prime(num):
            answer += 1

    return answer


def prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True