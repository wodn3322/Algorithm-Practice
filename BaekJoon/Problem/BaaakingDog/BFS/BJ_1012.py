import sys


def solution():
    answerList = []
    caseNum = int(sys.stdin.readline().strip())

    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFS():
        fieldSize = 1
        while len(queue):
            x, y = map(int, queue[0])
            del queue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                        fieldSize += 1
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
        answerList.append(fieldSize)

    for _ in range(caseNum):
        m, n, cabbageNum = map(int, sys.stdin.readline().strip().split())

        graph = [[0] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]

        for _ in range(cabbageNum):
            j, i = map(int, sys.stdin.readline().strip().split(' '))
            graph[i][j] = 1

        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1 and visited[i][j] == 0:
                    visited[i][j] = 1
                    queue.append([i, j])
                    BFS()
        sys.stdout.write((str(len(answerList)) + '\n'))
        answerList = []

    return


if __name__ == '__main__':
    solution()
