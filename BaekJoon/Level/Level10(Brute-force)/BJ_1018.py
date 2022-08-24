def solution():
    n, m = map(int, input().split())
    boardList = []

    for _ in range(n):
        boardList.append(input())

    reDraw = -1

    sampleBoard = []
    sample1 = ''
    sample2 = ''
    for i in range(8):
        sample1 += 'B'
        sample2 += 'W'
    sampleBoard.append(sample1)
    sampleBoard.append(sample2)

    for x in range(n - 7):
        for y in range(m - 7):
            count1 = 0
            count2 = 0
            for i in range(x, x + 8):
                for j in range(y, y + 8):
                    if (i + j) % 2 == 0:
                        if boardList[i][j] == 'B':
                            continue
                        else:
                            count1 += 1
                    else:
                        if boardList[i][j] == 'W':
                            continue
                        else:
                            count1 += 1
            for i in range(x, x + 8):
                for j in range(y, y + 8):
                    if (i + j) % 2 == 0:
                        if boardList[i][j] == 'W':
                            continue
                        else:
                            count2 += 1
                    else:
                        if boardList[i][j] == 'B':
                            continue
                        else:
                            count2 += 1
            count = count1 if count1 < count2 else count2
            if (reDraw > count and reDraw >= 0) or reDraw < 0:
                reDraw = count

    print(reDraw)

    return


if __name__ == '__main__':
    solution()
