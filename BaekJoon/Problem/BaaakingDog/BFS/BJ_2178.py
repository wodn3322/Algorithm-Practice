import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))

    graph = []
    for _ in range(n):
        graph.append(list(map(int, list(sys.stdin.readline().strip()))))

    visited = [[0] * m for _ in range(n)]

    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFS():
        while len(queue):
            x, y = map(int, queue[0])
            del queue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny])

    queue.append([0, 0])
    visited[0][0] = 1
    BFS()
    sys.stdout.write(str(visited[n - 1][m - 1]) + '\n')

    return


if __name__ == '__main__':
    solution()
