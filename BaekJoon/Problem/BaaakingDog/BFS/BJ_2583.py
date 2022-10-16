import sys


def solution():
    n, m, k = map(int, sys.stdin.readline().strip().split(' '))
    answer = []
    graph = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(k):
        startY, startX, endY, endX = map(int, sys.stdin.readline().strip().split(' '))
        for i in range(startX, endX):
            for j in range(startY, endY):
                graph[i][j] = 1

    def BFS():
        count = 1
        while len(queue):
            x, y = map(int, queue[0])
            del queue[0]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
                        count += 1
        answer.append(count)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and visited[i][j] == 0:
                visited[i][j] = 1
                queue.append([i, j])
                BFS()
    print(len(answer))
    answer.sort()
    for a in answer:
        print(a, end=' ')
    print()

    return


if __name__ == '__main__':
    solution()
