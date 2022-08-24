import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))

    twoCount = 0
    fiveCount = 0
    numFortwo = n
    while numFortwo != 0:
        twoCount += numFortwo // 2
        numFortwo = numFortwo // 2

    numFortwo = m
    while numFortwo != 0:
        twoCount -= numFortwo // 2
        numFortwo = numFortwo // 2

    numFortwo = n - m
    while numFortwo != 0:
        twoCount -= numFortwo // 2
        numFortwo = numFortwo // 2

    numForfive = n
    while numForfive != 0:
        fiveCount += numForfive // 5
        numForfive = numForfive // 5

    numForfive = m
    while numForfive != 0:
        fiveCount -= numForfive // 5
        numForfive = numForfive // 5

    numForfive = n - m
    while numForfive != 0:
        fiveCount -= numForfive // 5
        numForfive = numForfive // 5

    sys.stdout.write(str(min(twoCount, fiveCount)) + '\n')

    # total = 1
    # divideNum = 1
    # for i in range(m):
    #     total *= (n - i)
    #     divideNum *= (i + 1)
    # answer = total // divideNum
    # answerStringList = list(str(answer)[::-1])
    # zeroCount = 0
    #
    # for i in answerStringList:
    #     if i != "0":
    #         break
    #     else:
    #         zeroCount += 1
    # sys.stdout.write(str(zeroCount) + '\n')

    return


if __name__ == '__main__':
    solution()
