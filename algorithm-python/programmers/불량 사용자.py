import re
from itertools import permutations


def solution(user_id, banned_id):
    answer = set()
    banned_id = [ban.replace('*', '.') for ban in banned_id]

    perm = list(permutations(user_id, len(banned_id)))

    for p in perm:
        cnt = 0
        for idx, ban in enumerate(banned_id):
            if re.match(ban, p[idx]) and len(p[idx]) == len(ban):
                cnt += 1
        if cnt == len(p):
            answer.add(frozenset(p))

    return len(answer)
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
