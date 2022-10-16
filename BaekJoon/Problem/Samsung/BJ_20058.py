import sys

from collections import deque


def solution():
    n, q = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    n = 2 ** n
    visited = [[0] * n for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    lumpList = []

    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    levelList = list(map(int, sys.stdin.readline().strip().split(' ')))

    def rotate(x, y, size):
        rotateList = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                rotateList[i][j] = graph[x + size - 1 - j][y + i]
        for i in range(size):
            graph[x + i][y:y + size] = rotateList[i]

    def decreaseIce():
        deleteQueue = deque()
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 0:
                    continue
                count = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < n and 0 <= y < n:
                        if graph[x][y] >= 1:
                            count += 1
                if count < 3:
                    deleteQueue.append((i, j))

        while len(deleteQueue):
            x, y = deleteQueue.popleft()
            if graph[x][y] >= 1:
                graph[x][y] -= 1

    def BFS():
        count = 1
        while len(queue):
            x, y = map(int, queue.popleft())
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > 0 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
                        count += 1

        lumpList.append(count)

    for level in levelList:
        gridSize = 2 ** level
        if gridSize != 1:
            for i in range(n // gridSize):
                for j in range(n // gridSize):
                    rotate(i * gridSize, j * gridSize, gridSize)
        decreaseIce()

    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1 and visited[i][j] == 0:
                visited[i][j] = 1
                queue.append([i, j])
                BFS()

    totalIce = 0
    for g in graph:
        totalIce += sum(g)
    print(totalIce)
    if len(lumpList) != 0:
        print(max(lumpList))
    else:
        print(0)

    return


if __name__ == '__main__':
    solution()

# 3 1
# 1 2 3 4 5 6 7 8
# 9 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31 32
# 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48
# 49 50 51 52 53 54 55 56
# 57 58 59 60 61 62 63 64
# 1

# 3 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 2

# 3 4
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 2 0 3 2
