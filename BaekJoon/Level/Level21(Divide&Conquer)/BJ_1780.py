import sys

minusOneCount = 0
zeroCount = 0
oneCount = 0


def solution():
    size = int(sys.stdin.readline().strip())
    square = []
    for _ in range(size):
        square.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    def divide(x, y, n):
        global minusOneCount, zeroCount, oneCount
        color = square[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                divideN = n // 3
                if color != square[i][j]:
                    divide(x, y, divideN)
                    divide(x, y + divideN, divideN)
                    divide(x, y + divideN * 2, divideN)
                    divide(x + divideN, y, divideN)
                    divide(x + divideN, y + divideN, divideN)
                    divide(x + divideN, y + divideN * 2, divideN)
                    divide(x + divideN * 2, y, divideN)
                    divide(x + divideN * 2, y + divideN, divideN)
                    divide(x + divideN * 2, y + divideN * 2, divideN)
                    return
        if color == -1:
            minusOneCount += 1
        elif color == 0:
            zeroCount += 1
        else:
            oneCount += 1

    divide(0, 0, size)

    sys.stdout.write(str(minusOneCount) + '\n')
    sys.stdout.write(str(zeroCount) + '\n')
    sys.stdout.write(str(oneCount) + '\n')

    return


if __name__ == '__main__':
    solution()
