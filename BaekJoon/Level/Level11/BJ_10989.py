import sys


def solution():
    count = int(sys.stdin.readline())
    numList = [0] * 10001
    for _ in range(count):
        numList[int(sys.stdin.readline())] += 1

    for i in range(10001):
        if numList[i] != 0:
            for _ in range(numList[i]):
                sys.stdout.write(str(i) + '\n')

    # for i in range(count):
    #     numList[i] = int(sys.stdin.readline())
    #
    # maxNum = max(numList)
    # countingArr = [0] * (maxNum + 1)
    #
    # for i in numList:
    #     countingArr[i] += 1
    # answerList = []
    # for i in range(len(countingArr)):
    #     for _ in range(countingArr[i]):
    #         answerList.append(i)
    #
    # for i in answerList:
    #     sys.stdout.write(str(i) + '\n')

    # countingSumArr = [0] * (maxNum + 1)
    #
    # for i in range(len(countingArr)):
    #     countingSumArr[i] = (sum(countingArr[:i + 1]))
    #
    # answerList = [0] * count
    # for i in numList:
    #     answerList[countingSumArr[i] - 1] = i
    #     countingSumArr[i] -= 1
    #
    # for i in answerList:
    #     sys.stdout.write(str(i) + '\n')

    return


if __name__ == '__main__':
    solution()
