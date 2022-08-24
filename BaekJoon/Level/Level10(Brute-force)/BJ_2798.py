def solution():
    cardCount, targetNum = map(int, input().split(" "))
    cardList = list(map(int, input().split(' ')))
    sumMax = 0
    for i in range(cardCount):
        for j in range(i + 1, cardCount):
            for k in range(j + 1, cardCount):
                if sumMax < cardList[i] + cardList[j] + cardList[k] <= targetNum:
                    sumMax = cardList[i] + cardList[j] + cardList[k]

    print(sumMax)

    return


if __name__ == '__main__':
    solution()
