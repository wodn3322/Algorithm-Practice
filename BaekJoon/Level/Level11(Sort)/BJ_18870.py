# 시간초과 유의
# 비교를 없애고 sort내장함수로 정렬 후 index로 xi보다 적은 수의 개수를 표현

import sys


def solution():
    numCount = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().split(' ')))

    removeList = sorted(list(set(numList)))
    numDict = {}
    for i in range(len(removeList)):
        numDict[removeList[i]] = i

    for num in numList:
        sys.stdout.write(str(numDict[num]) + ' ')


    # 비교로 인해 시간 초과
    # compressList = [0] * numCount
    # setList = list(set(numList))
    # numDict = {}
    # for i in range(numCount):
    #     tempList = []
    #     if numList[i] in numDict:
    #         compressList[i] = numDict[numList[i]]
    #         continue
    #
    #     for j in setList:
    #         if numList[i] > j and j not in tempList:
    #             tempList.append(j)
    #             compressList[i] += 1
    #     numDict[numList[i]] = compressList[i]

    # for i in compressList:
    #     sys.stdout.write(str(i) + ' ')

    return


if __name__ == '__main__':
    solution()
