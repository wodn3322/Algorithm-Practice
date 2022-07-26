import sys


def solution():
    dictNum, pocketmonNum = map(int, sys.stdin.readline().split(' '))
    pocketDictString = {}
    pocketDictNum = {}
    pocketList = [''] * pocketmonNum
    for i in range(dictNum):
        pocketmon = sys.stdin.readline().strip()
        pocketDictString[pocketmon] = i
        pocketDictNum[i] = pocketmon
    for i in range(pocketmonNum):
        pocketList[i] = sys.stdin.readline().strip()

    answerList = []
    for pocketmon in pocketList:
        if not pocketmon.isdigit():
            answerList.append(pocketDictString[pocketmon] + 1)
        else:
            answerList.append(pocketDictNum[int(pocketmon) - 1])
    for i in answerList:
        sys.stdout.write(str(i) + '\n')

    return


if __name__ == '__main__':
    solution()
