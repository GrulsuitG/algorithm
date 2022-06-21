def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))  # 주어진 배열을 길이순으로 정렬
    prefix = dict()  # 접두사를 관리하는 dictionary
    length = []  # 이전에 등록된 번호들의 길이를 관리하는 list
    cur_len = len(phone_book[0])
    for number in phone_book:
        # 만약 길이가 늘어난 경우 관리 목록에 길이를 추가해준다.
        if len(number) != cur_len:
            length.append(cur_len)
            cur_len = len(number)
        # 현재 번호에서 등록된길이별로 접두사를 관리하는 dict에 있는지 확인 해준다.
        for l in length:
            # 만약 prefix에 있을 경우 False를 반환
            if number[:l] in prefix:
                return False

            # dictionary에 현재 번호 추가
        prefix[number] = True

    # 모든 번호를 다 돌았을 때 접두사 중복이 없는 경우 True 반환
    return True


def best(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True