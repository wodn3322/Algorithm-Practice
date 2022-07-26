def solution():
    hanoiNum = int(input())
    moveCount =0
    moveList =[]
    pollList =[[],[],[]]
    for i in range(1,hanoiNum+1):
        pollList[0].append(i)
    answerList = pollList[0]
    print(pollList)

    while True:
        if pollList[2]==answerList:
            break
        # for p in range(hanoiNum):


    return


if __name__ == '__main__':
    solution()
