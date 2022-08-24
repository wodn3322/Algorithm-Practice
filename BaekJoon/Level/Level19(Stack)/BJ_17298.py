import sys


def solution():
    numCount = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().strip().split(' ')))

    rightBigNumStack = []
    answerList = [-1]*numCount

    for i in range(numCount):
        while rightBigNumStack:
            if numList[i] > numList[rightBigNumStack[-1]]:
                answerList[rightBigNumStack.pop()] = numList[i]
            else:
                break
        rightBigNumStack.append(i)

    # print(*answerList)
    for answer in answerList:
        sys.stdout.write(str(answer)+' ')

    # 시간초과
    # answerList = [0]*numCount
    # answerList[numCount-1]= -1
    # bigNumList = []
    # bigNumList.insert(0,numList[numCount-1])
    # for i in range(numCount-1):
    #     if numList[numCount-1-i] > numList[numCount-i-2]:
    #         answerList[numCount-i-2] = numList[numCount-1-i]
    #         if numList[numCount - i - 1] not in bigNumList:
    #             bigNumList.insert(0,numList[numCount - i - 1])
    #     else:
    #         for n in bigNumList:
    #             if numList[numCount-i-2]<n:
    #                 answerList[numCount-i-2] = n
    #         if answerList[numCount-i-2]==0:
    #             answerList[numCount-i-2] = -1
    #             bigNumList.insert(0,numList[numCount-i-2])
    #         else:
    #             answerList[numCount-i-2]= bigNumList[0]
    #
    # for answer in answerList:
    #     sys.stdout.write(str(answer)+' ')

    # reverseList = numList[::-1]
    # rigthBigList = [0] * numCount
    #
    # bigNum = reverseList[0]
    # rigthBigList[numCount-1] = -1
    # for i in range( numCount-1):
    #     if bigNum > reverseList[i] or i ==0:
    #         if reverseList[i] > reverseList[i + 1]:
    #             rigthBigList[(numCount - 2 - i)] = reverseList[i]
    #         else:
    #             if bigNum < reverseList[i+1]:
    #                 bigNum = reverseList[i+1]
    #                 rigthBigList[(numCount - 2 - i)] = -1
    #             else:
    #                 rigthBigList[(numCount - 2 - i)] = bigNum
    #     else:
    #         rigthBigList[(numCount - 2- i)] = -1
    #
    # for num in rigthBigList:
    #     sys.stdout.write(str(num) + ' ')

    # 시간 초과
    # answerList = [0] * numCount
    # for i in range(numCount):
    #     if numList[i] > rigthBigList[i]:
    # for i in range(numCount):
    #     rigthList = numList[i:]
    #     standard = rigthList[0]
    #     for j in range(len(rigthList)):
    #         if i == (numCount-1):
    #             answerList[i] = -1
    #         if rigthList[j]>standard:
    #             answerList[i] = rigthList[j]
    #             break
    #
    #         if j == (len(rigthList)-1):
    #             answerList[i] = -1
    # for answer in answerList:
    #     sys.stdout.write(str(answer) + ' ')

    return


if __name__ == '__main__':
    solution()
