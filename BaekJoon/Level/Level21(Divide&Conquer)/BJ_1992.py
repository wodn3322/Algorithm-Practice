import sys

squareString = ''


def solution():
    size = int(sys.stdin.readline().strip())
    square = []

    for _ in range(size):
        square.append(list(map(int, list(sys.stdin.readline().strip()))))


    def divide(x, y, n):
        global squareString
        color = square[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if color != square[i][j]:
                    squareString+='('
                    halfN = n // 2
                    divide(x, y, halfN)
                    divide(x, y + halfN, halfN)
                    divide(x + halfN, y, halfN)
                    divide(x + halfN, y + halfN, halfN)
                    squareString+=')'
                    return
        squareString+=f'{color}'

    divide(0,0,size)

    sys.stdout.write(squareString+'\n')
    return


if __name__ == '__main__':
    solution()
