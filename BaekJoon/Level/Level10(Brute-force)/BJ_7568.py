def solution():
    caseNum = int(input())
    caseList = []
    caseScoreList = []
    for _ in range(caseNum):
        caseList.append(list(map(int, input().split(' '))))
        caseScoreList.append(1)

    for i in range(caseNum):
        for j in range(i + 1, caseNum):
            if caseList[i][0] > caseList[j][0] and caseList[i][1] > caseList[j][1]:
                caseScoreList[j] += 1
            elif caseList[i][0] < caseList[j][0] and caseList[i][1] < caseList[j][1]:
                caseScoreList[i] += 1

    for i in caseScoreList:
        print(i, end=' ')

    return


if __name__ == '__main__':
    solution()
