import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def solution():
    m, n = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    queue = deque()
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i, j])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFS():
        while len(queue):
            # y, x = queue[0][0], queue[0][1]
            # del queue[0]
            y, x = map(int, queue.popleft())
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if graph[ny][nx] == 0:
                        graph[ny][nx] = graph[y][x] + 1
                        queue.append([ny, nx])

    BFS()
    maxDay = 0

    for g in graph:
        if 0 in g:
            sys.stdout.write(str(-1) + '\n')
            return
        if maxDay < max(g):
            maxDay = max(g)
    sys.stdout.write(str(maxDay - 1) + '\n')

    return


if __name__ == '__main__':
    solution()
