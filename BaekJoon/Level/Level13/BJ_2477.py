import sys


def solution():
    melonGrow = int(sys.stdin.readline().strip())
    fieldList = []

    for _ in range(6):
        fieldList.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    height, width = 0, 0
    maxHeightIndex, maxWidthIndex = 0, 0

    for i in range(6):
        if fieldList[i][0] == 1 or fieldList[i][0] == 2:
            if fieldList[i][1] > width:
                width = fieldList[i][1]
                maxWidthIndex = i
        else:
            if fieldList[i][1] > height:
                height = fieldList[i][1]
                maxHeightIndex = i
    total = width * height
    minusHeight = abs(fieldList[maxHeightIndex + 1][1] - fieldList[maxHeightIndex - 1][1] if maxHeightIndex != 5 else
                      fieldList[0][1] - fieldList[maxHeightIndex - 1][1])
    minusWidth = abs(fieldList[maxWidthIndex + 1][1] - fieldList[maxWidthIndex - 1][1] if maxWidthIndex != 5 else
                     fieldList[0][1] - fieldList[maxWidthIndex - 1][1])

    minusRegin = minusHeight * minusWidth
    sys.stdout.write(str((total - minusRegin) * melonGrow) + '\n')

    return


if __name__ == '__main__':
    solution()
