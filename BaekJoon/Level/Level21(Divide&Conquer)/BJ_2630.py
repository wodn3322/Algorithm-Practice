import sys

blueCount, whiteCount = 0, 0


def solution():
    size = int(sys.stdin.readline().strip())

    square = []

    for _ in range(size):
        square.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    def divide(x, y, n):
        global blueCount, whiteCount
        nowColor = square[y][x]
        for i in range(y, y + n):
            for j in range(x, x + n):
                if nowColor != square[i][j]:
                    halfN = n // 2
                    divide(x, y, halfN)
                    divide(x, y + halfN, halfN)
                    divide(x + halfN, y, halfN)
                    divide(x + halfN, y + halfN, halfN)
                    return
        if nowColor == 0:
            whiteCount += 1
        else:
            blueCount += 1

    divide(0, 0, size)

    sys.stdout.write(str(whiteCount) + '\n')
    sys.stdout.write(str(blueCount) + '\n')

    return


if __name__ == '__main__':
    solution()
