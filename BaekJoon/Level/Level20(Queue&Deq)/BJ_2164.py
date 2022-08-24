import sys


def solution():
    num = int(sys.stdin.readline().strip())
    cardList = []
    for i in range(1, num + 1):
        cardList.append(i)

    loopCount = 0
    popCount = 0
    while len(cardList) != 1:
        if loopCount % 2 == 1:
            cardList.append(cardList[popCount])
        popCount += 1
        loopCount += 1
        if popCount == len(cardList):
            break

    sys.stdout.write(str(cardList[popCount - 1]) + '\n')

    return


if __name__ == '__main__':
    solution()
