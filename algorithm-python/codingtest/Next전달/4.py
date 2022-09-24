from collections import defaultdict


def solution(invitationPairs):
    invitations = defaultdict(list)
    point = defaultdict(int)
    for pair in invitationPairs:
        invitations[pair[0]].append(pair[1])

    for first, firstList in invitations.items():
        point[first] += len(firstList) * 10
        for second in firstList:
            secondList = invitations[second]
            point[first] += len(secondList) * 3
            for third in secondList:
                thirdList = invitations[third]
                point[first] += len(thirdList)
    return point

solution(
[[1, 2], [3, 4]])