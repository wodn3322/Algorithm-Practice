import sys


def solution():
    answer = []
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    graph = []

    visited = [[0] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    queue = []

    def BFS():
        count = 0
        while len(queue):
            x, y = map(int, queue[0])
            del queue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
                        count += 1
        if count == 0:
            count = 1
        answer.append(count)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                queue.append([i, j])
                BFS()

    sys.stdout.write(str(len(answer)) + '\n')
    if len(answer) == 0:
        sys.stdout.write('0\n')
    else:
        sys.stdout.write(str(max(answer)) + '\n')

    return


if __name__ == '__main__':
    solution()
