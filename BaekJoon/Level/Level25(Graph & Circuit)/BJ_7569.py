import sys
from collections import deque

sys.setrecursionlimit(10**6)

def solution():
    m, n, h = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    queue = deque()
    for i in range(h):
        layer = []
        for j in range(n):
            layer.append(list(map(int, sys.stdin.readline().strip().split(' '))))
            for l in range(m):
                if layer[j][l] == 1:
                    queue.append([i, j, l])
        graph.append(layer)

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    def BFS():
        while len(queue):
            z, y, x = map(int, queue.popleft())
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                    if graph[nz][ny][nx] == 0:
                        graph[nz][ny][nx] = graph[z][y][x] + 1
                        queue.append([nz,ny,nx])

    BFS()
    answer = 0
    for layer in graph:
        for line in layer:
            if 0 in line:
                sys.stdout.write(str(-1) + '\n')
                return
            if answer < max(line):
                answer = max(line)

    sys.stdout.write(str(answer-1) + '\n')

    return


if __name__ == '__main__':
    solution()
