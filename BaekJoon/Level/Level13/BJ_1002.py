import sys


def solution():
    caseCount = int(sys.stdin.readline().strip())
    caseList = []
    for i in range(caseCount):
        caseList.append(list(map(int, sys.stdin.readline().strip().split(' '))))
    answerList = [0] * caseCount

    for c in range(caseCount):
        if ((caseList[c][0]-caseList[c][3])**2 + (caseList[c][1]-caseList[c][4])**2)**(1/2) == 0 and caseList[c][2]== caseList[c][5]:
            answerList[c]=-1
        elif ((caseList[c][0]-caseList[c][3])**2 + (caseList[c][1]-caseList[c][4])**2)**(1/2) == caseList[c][2]+caseList[c][5]:
            answerList[c]=1
        elif ((caseList[c][0]-caseList[c][3])**2 + (caseList[c][1]-caseList[c][4])**2)**(1/2) == abs(caseList[c][2]-caseList[c][5]):
            answerList[c]=1
        elif abs(caseList[c][2]-caseList[c][5])<((caseList[c][0]-caseList[c][3])**2 + (caseList[c][1]-caseList[c][4])**2 )**(1/2)< abs(caseList[c][2]+caseList[c][5]):
            answerList[c]=2
        else:
            answerList[c]=0

        # 시간초과
        #
        # leeCase = []
        # joCase = []
        # for x in range(caseList[c][0] - caseList[c][2], caseList[c][0] + caseList[c][2] + 1):
        #     for y in range(caseList[c][1] - caseList[c][2], caseList[c][1] + caseList[c][2] + 1):
        #         if x + y > caseList[c][2]:
        #             if (caseList[c][0] - x) ** 2 + (caseList[c][1] - y) ** 2 == caseList[c][2] ** 2:
        #                 leeCase.append([x, y])
        #
        # for x in range(caseList[c][3] - caseList[c][5], caseList[c][3] + caseList[c][5] + 1):
        #     for y in range(caseList[c][4] - caseList[c][5], caseList[c][4] + caseList[c][2] + 1):
        #         if x+ y > caseList[c][5]:
        #             if (caseList[c][3] - x) ** 2 + (caseList[c][4] - y) ** 2 == caseList[c][5] ** 2:
        #                 joCase.append([x, y])
        # for l in leeCase:
        #     if l in joCase:
        #         answerList[c] += 1

    for i in answerList:
        sys.stdout.write(str(i) + '\n')

    return


if __name__ == '__main__':
    solution()
