import sys


def solution():
    caseNum = int(sys.stdin.readline().strip())

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    def BFS():
        while len(queue):
            x, y = map(int, queue[0])
            del queue[0]
            if x == targetX and y == targetY:
                sys.stdout.write(str(graph[x][y]) + "\n")
                return
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append([nx, ny])

    for _ in range(caseNum):
        queue = []

        n = int(sys.stdin.readline().strip())
        graph = [[0] * n for _ in range(n)]
        x, y = map(int, sys.stdin.readline().strip().split(' '))
        targetX, targetY = map(int, sys.stdin.readline().strip().split(' '))
        queue.append([x, y])
        BFS()

    return


if __name__ == '__main__':
    solution()
