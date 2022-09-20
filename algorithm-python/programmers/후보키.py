from itertools import combinations


def solution(relation):
    candidate = [i for i in range(len(relation[0]))]

    combi = []
    for i in range(1, len(candidate) + 1):
        combi += list(combinations(candidate, i))

    answer = []
    for comb in combi:
        item = [tuple([tuple_[idx] for idx in comb]) for tuple_ in relation]
        if len(item) == len(set(item)):
            unique = True
        else:
            unique = False

        for col in answer:
            if set(col).issubset(set(comb)):
                unique = False
                break

        if unique: answer.append(comb)


    return len(answer)

a = solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
print(a)