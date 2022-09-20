def solution(files):
    fileList = []
    for file in files:
        start, end = -1, -1
        for idx, char in enumerate(file):
            if char.isdigit():
                if start == -1:
                    start = idx
                    end = idx
                else:
                    end = idx
            if end != -1 and not char.isdigit():
                break
        head, number = file[:start].lower(), int(file[start:end + 1])
        fileList.append([head, number, file])

    fileList.sort(key=lambda x: (x[0], x[1]))
    answer = [file[2] for file in fileList]
    return answer

import re


def best(files):
    def key_function(fn):
        head, number, tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)', fn).groups()
        return [head, int(number)]

    return sorted(files, key=lambda x: key_function(x.lower()))


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
