import sys

from collections import deque


def solution():
    gearNum = int(sys.stdin.readline().strip())

    l, r = 6, 2
    gearList = []
    commandList = []
    for _ in range(gearNum):
        gearList.append(deque(list(map(int, list(sys.stdin.readline().strip())))))
    commandNum = int(sys.stdin.readline().strip())

    for _ in range(commandNum):
        commandList.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    for command in commandList:
        gear = command[0] - 1
        gearRotateList = [0] * gearNum
        gearRotateList[gear] = command[1]
        # left check
        while gear != 0:
            if gearList[gear - 1][r] == gearList[gear][l]:
                gearRotateList[gear - 1] = 0
            else:
                if gearRotateList[gear] == 1:
                    gearRotateList[gear - 1] = -1
                elif gearRotateList[gear] == -1:
                    gearRotateList[gear - 1] = 1
                else:
                    gearRotateList[gear - 1] = 0
            gear -= 1
        # right check
        gear = command[0] - 1
        while gear < gearNum - 1:
            if gearList[gear][r] == gearList[gear + 1][l]:
                gearRotateList[gear + 1] = 0
            else:
                if gearRotateList[gear] == 1:
                    gearRotateList[gear + 1] = -1
                elif gearRotateList[gear] == -1:
                    gearRotateList[gear + 1] = 1
                else:
                    gearRotateList[gear + 1] = 0
            gear += 1
        for i in range(gearNum):
            gearList[i].rotate(gearRotateList[i])

    answer = 0
    for g in gearList:
        if g[0] == 1:
            answer += 1
    sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
