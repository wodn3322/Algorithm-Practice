import sys

from collections import deque


def solution():
    m, n = map(int, sys.stdin.readline().strip().split(' '))
    graph = []

    visited = [[0] * m for _ in range(n)]
    # queue = []
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i, j])

    def BFS():
        global answer
        while len(queue):
            x, y = map(int, queue.popleft())
            # x, y = map(int, queue[0])
            # del queue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append([nx, ny])
                    elif graph[nx][ny] > 0:
                        graph[nx][ny] = min(graph[nx][ny], graph[x][y] + 1)

        day = 0
        for g in graph:
            if g.count(0) == 0:
                day = max(day, max(g))
            else:
                sys.stdout.write('-1\n')
                return
        sys.stdout.write(str(day - 1) + '\n')

    BFS()

    return


if __name__ == '__main__':
    solution()
