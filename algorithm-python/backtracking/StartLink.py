# 백준 14889번

from itertools import combinations

num = int(input())
# input() -> sys.stdin.readline()

table = []
for i in range(num):
    table.append(list(map(int, input().split())))

# --> table = [list(map(int, input().split())) for _ in range(num)]


# Best Solve

# X 의 능력치를 X와 다른 팀원들의 시너지의 합으로 생각할 수 있음
# 즉 table 에서 row 와 column 의 합
# --> 이를 zip 함수를 통해서 구현
newstat = [sum(i) + sum(j) for i, j in zip(table, zip(*table))]

# 전체 능력치는 각각의 능력치를 더한 후 2로 나눠주기(중복제거)
allstat = sum(newstat) // 2

result = 65535  # 2^16 -1

# 각각의 차이를 구하는 방식이 아닌 두 팀의 합산을 구해 총합에서 빼는 방식
# --> [:-1] 까지로 중복 제거 가능
for l in combinations(newstat[:-1], num // 2):
    result = min(result, abs(allstat - sum(l)))

print(result)

# 나의 풀이
# 문제를 있는 그대로 접근
# 단순화 할 수 있는 생각 필요


# def calcStat(team):
#     comb = set(combinations(team, 2))
#     stat = 0
#     for memberA, memberB in comb:
#         stat += table[memberA][memberB]
#         stat += table[memberB][memberA]
#
#     return stat
#
# def makeTeam(num):
#     member = set(i for i in range(num))
#     comb = set(combinations(member, int(num/2)))
#     candidate = []
#     for item in comb:
#         if 0 in item:
#             candidate.append(item)
#
#
#     result = 65535
#     for teamA in candidate:
#         teamA = set(teamA)
#         teamB = member - teamA
#
#         diff = abs(calcStat(teamA) - calcStat(teamB))
#         result = min(result, diff)
#
#     print(result)

