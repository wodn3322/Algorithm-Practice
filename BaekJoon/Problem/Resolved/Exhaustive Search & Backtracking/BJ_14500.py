import sys
from collections import deque

answer = 0
count = 0


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def DFS(locX, locY, s):
        global answer, count
        if count == 4:
            answer = max(answer, s)
            return
        for i in range(4):
            nx = locX + dx[i]
            ny = locY + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    count += 1
                    DFS(nx, ny, s + graph[ny][nx])
                    count -= 1
                    visited[ny][nx] = 0

    def leftShape(locX, locY):
        global answer
        answerList = []
        if 0 < locX < (m - 1) and 0 < locY < (n - 1):
            for i in range(4):
                s = graph[locY][locX]
                for j in range(4):
                    if j != i:
                        s += graph[locY + dy[j]][locX + dx[j]]
                answerList.append(s)
            answer = max(answer, max(answerList))

        else:
            s = graph[locY][locX]
            for i in range(4):
                nx = locX + dx[i]
                ny = locY + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    s += graph[ny][nx]
            answer = max(answer,s)

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                visited[i][j] = 1
                DFS(j, i, 0)
                leftShape(j, i)
                visited[i][j] = 0
    sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
