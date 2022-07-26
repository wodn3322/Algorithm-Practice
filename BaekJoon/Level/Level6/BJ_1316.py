def solution():
    inputCount = int(input())
    inputStringList = []
    groupWordCount = inputCount

    for _ in range(inputCount):
        inputStringList.append(input())

    for i in inputStringList:
        word = ''
        useAlphaList = []
        for s in list(i):
            if word == '':
                word += s
                useAlphaList.append(s)
                continue

            if (s not in useAlphaList) and word[-1] != s:
                useAlphaList.append(s)
                word += s
            elif (s in useAlphaList) and word[-1] == s:
                word += s
            elif (s in useAlphaList) and word[-1] != s:
                groupWordCount -= 1
                break

    print(groupWordCount)
    return


if __name__ == '__main__':
    solution()
