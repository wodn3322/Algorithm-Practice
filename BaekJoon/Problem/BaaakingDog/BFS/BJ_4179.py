import sys

from collections import deque


def solution():
    answer = []

    n, m = map(int, sys.stdin.readline().strip().split(' '))

    fireMap = [[0] * m for _ in range(n)]
    jMap = [[0] * m for _ in range(n)]

    visitedFire = [[0] * m for _ in range(n)]
    visitedJ = [[0] * m for _ in range(n)]
    fQueue = deque()
    jQueue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph = []
    for i in range(n):
        graph.append(list(sys.stdin.readline().strip()))
        for j in range(m):
            if graph[i][j] == 'J':
                jQueue.append([i, j])
                jMap[i][j] = 1
            if graph[i][j] == 'F':
                fQueue.append([i, j])
                fireMap[i][j] = 1

    def BFS():
        # fire
        while len(fQueue):
            x, y = map(int, fQueue.popleft())
            # x, y = map(int, fQueue[0])
            # del fQueue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if (graph[nx][ny] == '.' or graph[nx][ny] == 'J') and fireMap[nx][ny] == 0 and visitedFire[nx][ny] == 0:
                        visitedFire[nx][ny] = 1
                        fireMap[nx][ny] = fireMap[x][y] + 1
                        fQueue.append([nx, ny])

        # j
        while len(jQueue):
            x, y = map(int, jQueue.popleft())
            # x, y = map(int, jQueue[0])
            # del jQueue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == '.':
                        if jMap[nx][ny] == 0 and visitedJ[nx][ny] == 0:
                            visitedJ[nx][ny] = 1
                            jMap[nx][ny] = jMap[x][y] + 1
                            jQueue.append([nx, ny])

        # for f in fireMap:
        #     print(f)
        # print()
        # for j in jMap:
        #     print(j)

        for i in range(n):
            for j in range(m):
                if not (0 < i < n - 1 and 0 < j < m - 1) and jMap[i][j] != 0:
                    if (jMap[i][j] < fireMap[i][j]) or fireMap[i][j] == 0:
                        answer.append(jMap[i][j])
                # if (j == 0 or j == m - 1):
                #     if jMap[i][j] < fireMap[i][j] :
                #         answer.append(jMap[i][j])

        if len(answer):
            sys.stdout.write(str(min(answer)) + '\n')
        else:
            sys.stdout.write('IMPOSSIBLE\n')

    BFS()

    # 시간 초과
    # def checkMap(nowMap):
    #     stackList = []
    #     for i in range(n):
    #         for j in range(m):
    #             if nowMap[i][j] == 'F':
    #                 for k in range(4):
    #                     nx = i + dx[k]
    #                     ny = j + dy[k]
    #                     if 0 <= nx < n and 0 <= ny < m:
    #                         if nowMap[nx][ny] != '#':
    #                             stackList.append([nx, ny])
    #     for s in stackList:
    #         x, y = map(int, s)
    #         nowMap[x][y] = 'F'
    #     return nowMap
    #
    # def BFS():
    #     while len(queue):
    #         x, y, t, nMap = queue[0][0], queue[0][1], queue[0][2], queue[0][3]
    #         del queue[0]
    #         changeMap = checkMap(nMap)
    #         for i in range(4):
    #             nx = x + dx[i]
    #             ny = y + dy[i]
    #             if 0 <= nx < n and 0 <= ny < m:
    #                 if (nx == 0 or nx == n - 1 or ny == 0 or ny == m - 1) and nMap[nx][ny] == '.':
    #                     answer.append(t + 1)
    #                     continue
    #                 else:
    #                     if changeMap[nx][ny] == '.' and visited[nx][ny] == 0:
    #                         visited[nx][ny] = 1
    #                         changeMap[nx][ny] = 'J'
    #                         if changeMap[x][y] == 'J':
    #                             changeMap[x][y] = '.'
    #                         queue.append([nx, ny, t + 1, changeMap])
    #     if len(answer):
    #         sys.stdout.write(str(min(answer)) + '\n')
    #     else:
    #         sys.stdout.write('IMPOSSIBLE\n')
    #
    # queue.append([jX, jY, 1, graph])
    # BFS()

    return


if __name__ == '__main__':
    solution()
