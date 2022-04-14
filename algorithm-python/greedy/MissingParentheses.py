#백준 1541번
import sys

#두번째 풀이
exp = sys.stdin.readline().split('-')

arr = [sum(map(int, e.split('+'))) for e in exp]
result = arr[0]

for i in arr[1:]:
    result -= i

print(result)

# 처음 풀이
# num = []
# op = ['+']
#
# temp = ''
# for e in exp:
#     if e.isdigit():
#         temp += e
#     else:
#         op.append(e)
#         num.append(int(temp))
#         temp = ''
#
# for i in range(1, len(op)):
#     if op[i-1] == '-' and op[i] == '+':
#         op[i] = '-'
#
# result = 0
# for i in range(len(num)):
#     if op[i] == '+':
#         result += num[i]
#     elif op[i] == '-':
#         result -= num[i]
#
# print(result)