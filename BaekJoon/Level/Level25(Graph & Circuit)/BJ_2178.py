import sys

sys.setrecursionlimit(10 ** 6)


def solution():
    global count
    n, m = map(int, sys.stdin.readline().strip().split(' '))

    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFS(x, y):
        queue = []
        queue.append([x, y])

        while len(queue) != 0:
            x, y = map(int, queue[0])
            queue.remove([x, y])
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                    queue.append([nx, ny])
                    graph[ny][nx] = graph[y][x] + 1

    BFS(0, 0)

    sys.stdout.write(str(graph[n - 1][m - 1]) + '\n')

    return


if __name__ == '__main__':
    solution()
