def solution():
    caseNum = int(input())
    caseList = []
    for _ in range(caseNum):
        a = int(input())
        b = int(input())
        caseList.append(([a, b]))

    for case in caseList:
        floorList = [i for i in range(1, case[1] + 1)]
        for i in range(1, case[0] + 1):
            nextFloorSum = 0
            for j in range(case[1]):
                nextFloorSum += floorList[j]
                floorList[j] = nextFloorSum
        print(floorList[-1])
    return


if __name__ == '__main__':
    solution()
