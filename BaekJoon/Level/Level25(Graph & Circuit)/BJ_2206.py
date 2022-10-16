import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    visited = [[[0] * m for _ in range(n)] for _ in range(2)]
    blockCheck = 1

    for _ in range(n):
        graph.append(list(map(int, list(sys.stdin.readline().strip()))))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    visited[blockCheck][0][0] = 1
    queue.append([0, 0, blockCheck])

    def BFS():
        while len(queue):
            x, y, b = map(int, queue.popleft())

            if x == m - 1 and y == n - 1:
                sys.stdout.write(str(visited[b][y][x]) + '\n')
                return

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if graph[ny][nx] == 0 and visited[b][ny][nx] == 0:
                        visited[b][ny][nx] = visited[b][y][x] + 1
                        queue.append([nx, ny, b])
                    elif graph[ny][nx] == 1 and b == 1:
                        visited[b - 1][ny][nx] = visited[b][y][x] + 1
                        queue.append([nx, ny, b - 1])
        return sys.stdout.write(str(-1) + '\n')

    BFS()

    return


if __name__ == '__main__':
    solution()
