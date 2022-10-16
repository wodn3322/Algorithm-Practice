import sys

from collections import deque


def solution():
    caseNum = int(sys.stdin.readline().strip())

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def FBFS():
        while len(fQueue):
            x, y = map(int, fQueue.popleft())
            if fVisited[x][y] == 0:
                fVisited[x][y] = 1
            # x, y = map(int, fQueue[0])
            # del fQueue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] != '#' and fVisited[nx][ny] == 0:
                        fVisited[nx][ny] = fVisited[x][y] + 1
                        fQueue.append([nx, ny])

    def SBFS():
        while len(sQueue):
            x, y = map(int, sQueue.popleft())
            if sVisited[x][y] == 0:
                sVisited[x][y] = 1
            # x, y = map(int, sQueue[0])
            # del sQueue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == '.' and sVisited[nx][ny] == 0:
                        sVisited[nx][ny] = sVisited[x][y] + 1
                        sQueue.append([nx, ny])

    for _ in range(caseNum):
        m, n = map(int, sys.stdin.readline().strip().split(' '))
        graph = []
        sQueue = deque()
        fQueue = deque()
        fVisited = [[0] * m for _ in range(n)]
        sVisited = [[0] * m for _ in range(n)]
        for i in range(n):
            graph.append(list(sys.stdin.readline().strip()))
            for j in range(m):
                if graph[i][j] == '@':
                    sQueue.append([i, j])
                if graph[i][j] == '*':
                    fQueue.append([i, j])
        fireCheck = True if len(fQueue) else False

        FBFS()
        SBFS()

        # print(fVisited)
        # print(sVisited)

        timeList = []
        for i in range(n):
            for j in range(m):
                if not (0 < i < n - 1 and 0 < j < m - 1):
                    if fireCheck:
                        if sVisited[i][j] < fVisited[i][j] and sVisited[i][j] != 0:
                            timeList.append(sVisited[i][j])
                        elif fVisited[i][j] == 0 and sVisited[i][j] != 0:
                            timeList.append(sVisited[i][j])
                    else:
                        if sVisited[i][j] != 0:
                            timeList.append(sVisited[i][j])
        if len(timeList):
            sys.stdout.write(str(min(timeList)) + '\n')
        else:
            sys.stdout.write('IMPOSSIBLE\n')

    return


if __name__ == '__main__':
    solution()
