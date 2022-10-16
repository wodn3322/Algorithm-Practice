import sys


def solution():
    n = int(sys.stdin.readline().strip())
    graph = []

    for _ in range(n):
        graph.append(list(sys.stdin.readline().strip()))

    visitedBlind = [[0] * n for _ in range(n)]
    fieldBlind = []
    visited = [[0] * n for _ in range(n)]
    field = []

    queueBlind = []
    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFSBlind():
        fieldSize = 1
        while len(queueBlind):
            x, y, color = queueBlind[0][0], queueBlind[0][1], queueBlind[0][2]
            del queueBlind[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 'B':
                        if color == 'B' and visitedBlind[nx][ny] == 0:
                            visitedBlind[nx][ny] = 1
                            fieldSize += 1
                            queueBlind.append([nx, ny, color])
                    else:
                        if color != 'B' and visitedBlind[nx][ny] == 0:
                            visitedBlind[nx][ny] = 1
                            fieldSize += 1
                            queueBlind.append([nx, ny, color])
        fieldBlind.append(fieldSize)

    def BFS():
        fieldSize = 1
        while len(queue):
            x, y, color = queue[0][0], queue[0][1], queue[0][2]
            del queue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == color and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        fieldSize += 1
                        queue.append([nx, ny, color])
        field.append(fieldSize)

    for i in range(n):
        for j in range(n):
            if visitedBlind[i][j] == 0:
                queueBlind.append([i, j, graph[i][j]])
                BFSBlind()

            if visited[i][j] == 0:
                queue.append([i, j, graph[i][j]])
                BFS()

    sys.stdout.write(str(len(field)) + ' ' + str(len(fieldBlind)) + '\n')

    return


if __name__ == '__main__':
    solution()
