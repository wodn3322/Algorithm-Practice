import sys


def solution():
    data = []
    zeroList = []
    for i in range(9):
        data.append(list(map(int, sys.stdin.readline().strip().split(' '))))
        for j in range(9):
            if data[i][j] == 0:
                zeroList.append([i, j])

    def checkRow(indexX, num):
        for i in range(9):
            if data[indexX][i] == num:
                return 0
        return 1

    def checkCol(indexY, num):
        for i in range(9):
            if data[i][indexY] == num:
                return 0
        return 1

    def checkSquare(indexX, indexY, num):
        for i in range(3):
            for j in range(3):
                if data[indexX // 3 * 3 + i][indexY // 3 * 3 + j] == num:
                    return 0
        return 1

    def findNum(indexX, indexY):
        temp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(3):
            for j in range(3):
                if data[indexX // 3 * 3 + i][indexY // 3 * 3 + j] in temp:
                    temp.remove(data[indexX // 3 * 3 + i][indexY // 3 * 3 + j])
        return temp



    def backtracking(listdata):
        if len(listdata) == 0:
            for i in data:
                for j in i:
                    sys.stdout.write(str(j) + ' ')
                sys.stdout.write('\n')
            exit()
        else:
            x = listdata[0][0]
            y = listdata[0][1]
            numList = findNum(x, y)
            numList = list(set(numList) - set(data[x]))
            for num in numList:
                if checkCol(y, num):
                    data[x][y] = num
                    listdata.pop(0)
                    backtracking(listdata)
                    listdata.insert(0, [x, y])
                    data[x][y] = 0

    backtracking(zeroList)

    return


if __name__ == '__main__':
    solution()
