# 백준 11053번
import sys

# 나의 풀이
# 쉽지만 O(N^2)
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * N

for i in range(1, N):
    result = 0
    for j in range(i):
        if arr[i] > arr[j]:
            result = max(result, dp[j])
    dp[i] += result

print(max(dp))

# 남의 풀이
# Binary Search O(NlogN)
# A = list(map(int, sys.stdin.readline().split()))
#
# arr = [A[0]]
# for i in range(1, N):
#     h = A[i]
#
#     제일 마지막 원소보다 크면 수열에 추가
#     if arr[-1] < h:
#         arr.append(h)
#     아니면 수열에 들어갈 위치 찾기
#     else:
#         l = 0
#         r = len(arr)
#         m = 0
#
#         while l < r:
#             m = (l + r) // 2
#             if arr[m] < h:
#                 l = m + 1
#             else:
#                 r = m
#
#         arr[r] = h
#
