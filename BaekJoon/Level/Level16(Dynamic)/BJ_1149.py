import sys


def solution():
    houseNum = int(sys.stdin.readline().strip())
    colorWeightList = []

    for _ in range(houseNum):
        colorWeightList.append(list(map(int, sys.stdin.readline().strip().split())))

    for i in range(1, houseNum):
        colorWeightList[i][0] += min(colorWeightList[i - 1][1], colorWeightList[i - 1][2])
        colorWeightList[i][1] += min(colorWeightList[i - 1][0], colorWeightList[i - 1][2])
        colorWeightList[i][2] += min(colorWeightList[i - 1][0], colorWeightList[i - 1][1])

    sys.stdout.write(str(min(colorWeightList[houseNum - 1])) + '\n')

    return


if __name__ == '__main__':
    solution()
