import math


def solution(str1, str2):
    answer = 0

    str1List = []
    str2List = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1List.append(str1[i:i + 2].upper())

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2List.append(str2[i:i + 2].upper())

    if len(str1List) == 0 and len(str2List) == 0:
        answer = 65536
        return answer

    uniconList = []
    interList = []
    for i in str1List:
        uniconList.append(i)
        if i in str2List:
            interList.append(i)
            str2List.remove(i)

    for i in str2List:
        uniconList.append(i)

    answer = math.floor(len(interList) / len(uniconList) * 65536)
    print(answer)
    return answer


if __name__ == '__main__':
    a = 'FRANCE'
    b = 'french'
    solution(a, b)
