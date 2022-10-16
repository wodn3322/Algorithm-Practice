import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    commandList = []

    dx = [0, -1, - 1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    cross = [1, 3, 5, 7]

    cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    for _ in range(m):
        commandList.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    def checkCloud():
        newCloud = []
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0 and graph[i][j] >= 2:
                    graph[i][j] -= 2
                    newCloud.append([i, j])
                if visited[i][j] == 1:
                    visited[i][j] = 0
        return newCloud

    def moveCloud():
        moveCloud = []
        for c in cloud:
            x, y = map(int, c)
            nx = x + dx[d - 1] * (s % n)
            ny = y + dy[d - 1] * (s % n)
            if nx < 0:
                nx = n + nx
            if nx >= n:
                nx = nx - n
            if ny < 0:
                ny = n + ny
            if ny >= n:
                ny = ny - n
            visited[nx][ny] = 1
            graph[nx][ny] += 1
            moveCloud.append([nx, ny])
        return moveCloud

    def checkCross():
        waterList = []
        for c in cloud:
            x, y = map(int, c)
            water = 0
            for i in cross:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > 0:
                        water += 1
            waterList.append(water)

        for i in range(len(cloud)):
            x, y = map(int, cloud[i])
            graph[x][y] += waterList[i]

    visited = [[0] * n for _ in range(n)]
    for i in range(len(commandList)):
        if i != 0:
            cloud = checkCloud()
        d, s = map(int, commandList[i])
        cloud = moveCloud()
        checkCross()
        if i == len(commandList) - 1:
            cloud = checkCloud()

    answer = 0
    for g in graph:
        answer += sum(g)

    sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
