import sys


def solution():
    n = int(sys.stdin.readline().strip())

    graph = [[0] * n for _ in range(n)]

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    dataDict = dict()

    for _ in range(n ** 2):
        data = list(map(int, sys.stdin.readline().strip().split(' ')))
        dataDict[data[0]] = data[1:]

    def checkFav(num):
        # 좋아하는 학생수, 빈칸 수, x, y
        locData = [0, 0, 0, 0]
        zeroList = []
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 0:
                    favNum = 0
                    empty = 0
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[nx][ny] in dataDict[num]:
                                favNum += 1
                            elif graph[nx][ny] == 0:
                                empty += 1
                    if locData[0] == favNum:
                        if locData[1] == empty:
                            if locData[2] > i:
                                locData = [favNum, empty, i, j]
                            elif locData[2] == i:
                                if locData[3] > j:
                                    locData = [favNum, empty, i, j]
                        elif locData[1] < empty:
                            locData = [favNum, empty, i, j]
                    elif locData[0] < favNum:
                        locData = [favNum, empty, i, j]
        if locData.count(0) != 4:
            graph[locData[2]][locData[3]] = num
        else:
            for i in range(n):
                for j in range(n):
                    if graph[i][j] == 0:
                        graph[i][j] = num
                        return

    def checkGood():
        good = 0
        for i in range(n):
            for j in range(n):
                count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in dataDict[graph[i][j]]:
                            count += 1
                good += round(10 ** (count - 1))
        return good

    for k in dataDict:
        checkFav(k)
        # for g in graph:
        #     print(g)
        # print()
    answer = checkGood()

    sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
