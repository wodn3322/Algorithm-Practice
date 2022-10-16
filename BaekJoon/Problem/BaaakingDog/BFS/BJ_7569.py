import sys

from collections import deque


def solution():
    answer = 0
    m, n, l = map(int, sys.stdin.readline().strip().split(' '))

    graph = [[] for _ in range(l)]

    queue = deque()
    # queue = []
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    for i in range(l):
        for j in range(n):
            graph[i].append(list(map(int, sys.stdin.readline().strip().split(' '))))
            for k in range(m):
                if graph[i][j][k] == 1:
                    queue.append([i, j, k])

    def BFS():
        while len(queue):
            z, x, y, = map(int, queue.popleft())
            # z, x, y, = map(int, queue[0])
            # del queue[0]
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nz < l and 0 <= nx < n and 0 <= ny < m:
                    if graph[nz][nx][ny] == 0:
                        graph[nz][nx][ny] = graph[z][x][y] + 1
                        queue.append([nz, nx, ny])

    BFS()

    day = 0
    for i in range(l):
        for g in graph[i]:
            if g.count(0) == 0:
                day = max(day, max(g))
            else:
                day = -1
                sys.stdout.write(str(day) + '\n')
                return

    sys.stdout.write(str(day - 1) + '\n')

    return


if __name__ == '__main__':
    solution()
