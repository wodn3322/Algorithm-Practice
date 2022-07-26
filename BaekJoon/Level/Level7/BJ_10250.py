def solution():
    caseNum = int(input())
    caseList = []
    for _ in range(caseNum):
        caseList.append(list(map(int, input().split(" "))))

    for c in caseList:
        roomNum = c[2] // c[0]
        if c[2] % c[0] == 0:
            print(str(c[0]) + ('0' + str(roomNum) if roomNum < 10 else str(roomNum)))
        else:
            print(str(c[2] % c[0]) + ('0' + str(roomNum + 1) if roomNum + 1 < 10 else str(roomNum + 1)))

    return


if __name__ == '__main__':
    solution()
