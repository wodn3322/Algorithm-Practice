import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    graph = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    deleteMarbleList = [0] * 3

    startX, startY = n // 2, n // 2
    marbleCount = 0
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))
        marbleCount += (n - graph[i].count(0))

    magicList = []
    for _ in range(m):
        magicList.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    def deleteMarble(direct, speed):
        for i in range(1, speed + 1):
            nx = startX + dx[direct - 1] * i
            ny = startY + dy[direct - 1] * i
            graph[nx][ny] = 0

    def checkGrid():
        gridList = []
        loopCheck = 0
        directList = [[2, 1], [3, 0]]
        length = 1
        count = 0
        x = startX
        y = startY
        while True:
            for d in directList[loopCheck % 2]:
                for _ in range(length):
                    if x == 0 and y == 0:
                        return gridList
                    x += dx[d]
                    y += dy[d]
                    gridList.append(graph[x][y])
                    count += 1
                    if count == marbleCount:
                        return gridList
            loopCheck += 1
            length += 1

    def deleteContinue(cList):
        removeList = []
        removeCount = 0
        i = 0
        while i < (len(cList) - 3):
            removeList.append(i)
            for j in range(i + 1, len(cList)):
                if cList[j] == cList[i]:
                    removeList.append(j)
                else:
                    break
            if len(removeList) >= 4:
                deleteMarbleList[cList[i] - 1] += len(removeList)
                del cList[i:i + len(removeList)]
                removeCount += 1
            else:
                i += len(removeList)
            removeList = []
        if removeCount > 0:
            cList = deleteContinue(cList)
        return cList

    def remakeList(cList):
        newList = []
        a, b = 1, cList[0]
        i = 1
        while i < len(cList):
            if cList[i] == b:
                a += 1
            else:
                newList.append(a)
                newList.append(b)
                b = cList[i]
                a = 1
            i += 1
        if b != 0:
            newList.append(a)
            newList.append(b)
        return newList

    def fillGrid(cList):
        newGraph = [[0] * n for _ in range(n)]
        loopCheck = 0
        directList = [[2, 1], [3, 0]]
        length = 1
        count = 0
        x = startX
        y = startY
        if len(cList):
            while True:
                for d in directList[loopCheck % 2]:
                    for _ in range(length):
                        if x == 0 and y == 0:
                            return newGraph
                        x += dx[d]
                        y += dy[d]
                        newGraph[x][y] = cList[count]
                        count += 1
                        if (count == len(cList) or count == n ** 2):
                            return newGraph
                loopCheck += 1
                length += 1
        else:
            return newGraph

    for magic in magicList:
        d, s = map(int, magic)
        deleteMarble(d, s)
        checkList = checkGrid()
        zeroCount = checkList.count(0)
        for i in range(zeroCount):
            checkList.remove(0)
            marbleCount -= 1
        checkList = deleteContinue(checkList)
        if len(checkList):
            checkList = remakeList(checkList)
        marbleCount = len(checkList)
        graph = fillGrid(checkList)

    total = 0
    for i in range(len(deleteMarbleList)):
        total += (i + 1) * deleteMarbleList[i]
    print(total)
    return


if __name__ == '__main__':
    solution()
