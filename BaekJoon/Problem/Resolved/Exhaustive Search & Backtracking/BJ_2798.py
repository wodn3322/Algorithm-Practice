import sys


def solution():
    cardNum, maxNum = map(int, sys.stdin.readline().strip().split(' '))
    cardList = list(map(int, sys.stdin.readline().strip().split(' ')))
    answer = 0
    cardList.sort()

    for i in range(cardNum):
        for j in range(i+1, cardNum):
            for k in range(j+1, cardNum):
                cardSum = cardList[i] + cardList[j] + cardList[k]
                if cardSum <= maxNum:
                    if answer < cardSum:
                        answer = cardSum

    sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
