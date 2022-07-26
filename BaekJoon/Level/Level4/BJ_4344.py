def solution():
    caseLength = int(input())
    percentList = []
    for _ in range(caseLength):
        inputList = list(map(int, input().split(" ")))
        studentNum = inputList[0]
        scoreList = inputList[1:]
        avgScore = sum(scoreList) / studentNum
        overStu = 0
        for i in scoreList:
            if i > avgScore:
                overStu += 1
        percentList.append(str(format(round(overStu / studentNum * 100, 3), '.3f')) + "%")
    for i in percentList:
        print(i)
    return


if __name__ == '__main__':
    solution()
