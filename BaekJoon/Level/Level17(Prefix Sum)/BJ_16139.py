import sys


def solution():
    stringList = list(sys.stdin.readline().strip())
    caseNum = int(sys.stdin.readline().strip())
    caseList = []
    for _ in range(caseNum):
        caseList.append(list(sys.stdin.readline().strip().split(' ')))
    # setList = set(stringList)
    cumlativeList = [[0] * (len(stringList)) for _ in range(26)]

    # for s in setList:
    #     targetS = ord(s) - 97
    #     count = 0
    #     for i in range(len(stringList)):
    #         if stringList[i] == s:
    #             count += 1
    #             cumlativeList[targetS][i] = count
    #         else:
    #             cumlativeList[targetS][i] = count

    for i in range(26):
        loopalpha = chr(97 + i)
        count = 0
        for j in range(len(stringList)):
            if stringList[j] == loopalpha:
                count += 1
                cumlativeList[i][j] += count
            else:
                cumlativeList[i][j] = count

    # print(cumlativeList)

    for case in caseList:
        if int(case[1]) > 0:
            sys.stdout.write(
                str(cumlativeList[ord(case[0]) - 97][int(case[2])] - cumlativeList[ord(case[0]) - 97][int(case[1]) - 1]) + '\n')
        else:
            sys.stdout.write(str(cumlativeList[ord(case[0]) - 97][int(case[2])]) + '\n')
    return


if __name__ == '__main__':
    solution()
