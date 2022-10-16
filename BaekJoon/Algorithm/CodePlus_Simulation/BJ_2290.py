import sys


def solution():
    s, num = sys.stdin.readline().strip().split(' ')
    s = int(s)
    numList = list(map(int, list(num)))

    lcdList = []

    for _ in range(2 * s + 3):
        lcdList.append('')

    def appendRow(need, index):
        if need:
            for i in range(s + 2):
                if i == 0 or i == s + 1:
                    lcdList[index] += ' '
                else:
                    lcdList[index] += '-'
        else:
            for _ in range(s + 2):
                lcdList[index] += ' '
        lcdList[index] += ' '

    def appendCol(f, b, index):
        for j in range(s):
            for i in range(s + 2):
                if f and i == 0:
                    lcdList[index + j] += '|'
                elif b and i == s + 1:
                    lcdList[index + j] += '|'
                else:
                    lcdList[index + j] += ' '
            lcdList[index + j] += ' '

    def checkNum(n):
        if n == 1:
            appendRow(0, 0)
            appendCol(0, 1, 1)
            appendRow(0, s + 1)
            appendCol(0, 1, s + 2)
            appendRow(0, 2 * s + 2)
        elif n == 2:
            appendRow(1, 0)
            appendCol(0, 1, 1)
            appendRow(1, s + 1)
            appendCol(1, 0, s + 2)
            appendRow(1, 2 * s + 2)
        elif n == 3:
            appendRow(1, 0)
            appendCol(0, 1, 1)
            appendRow(1, s + 1)
            appendCol(0, 1, s + 2)
            appendRow(1, 2 * s + 2)
        elif n == 4:
            appendRow(0, 0)
            appendCol(1, 1, 1)
            appendRow(1, s + 1)
            appendCol(0, 1, s + 2)
            appendRow(0, 2 * s + 2)
        elif n == 5:
            appendRow(1, 0)
            appendCol(1, 0, 1)
            appendRow(1, s + 1)
            appendCol(0, 1, s + 2)
            appendRow(1, 2 * s + 2)
        elif n == 6:
            appendRow(1, 0)
            appendCol(1, 0, 1)
            appendRow(1, s + 1)
            appendCol(1, 1, s + 2)
            appendRow(1, 2 * s + 2)
        elif n == 7:
            appendRow(1, 0)
            appendCol(0, 1, 1)
            appendRow(0, s + 1)
            appendCol(0, 1, s + 2)
            appendRow(0, 2 * s + 2)
        elif n == 8:
            appendRow(1, 0)
            appendCol(1, 1, 1)
            appendRow(1, s + 1)
            appendCol(1, 1, s + 2)
            appendRow(1, 2 * s + 2)
        elif n == 9:
            appendRow(1, 0)
            appendCol(1, 1, 1)
            appendRow(1, s + 1)
            appendCol(0, 1, s + 2)
            appendRow(1, 2 * s + 2)
        elif n == 0:
            appendRow(1, 0)
            appendCol(1, 1, 1)
            appendRow(0, s + 1)
            appendCol(1, 1, s + 2)
            appendRow(1, 2 * s + 2)

    for n in numList:
        checkNum(n)

    for lcd in lcdList:
        print(lcd)

    return


if __name__ == '__main__':
    solution()
