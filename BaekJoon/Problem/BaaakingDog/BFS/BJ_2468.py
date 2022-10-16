import sys


def solution():
    n = int(sys.stdin.readline().strip())
    answer = 0
    graph = []
    maxH = 1

    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(n):
        locData = list(map(int, sys.stdin.readline().strip().split(' ')))
        graph.append(locData)
        if maxH < max(locData):
            maxH = max(locData)

    def BFS(heigth):
        while len(queue):
            x, y = map(int, queue[0])
            del queue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > heigth and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append([nx, ny])

    for h in range(0, maxH):
        visited = [[0] * n for _ in range(n)]
        partCount = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] > h and visited[i][j] == 0:
                    visited[i][j] = 1
                    queue.append([i, j])
                    BFS(h)
                    partCount += 1
        answer = max(answer, partCount)
    print(answer)
    return


if __name__ == '__main__':
    solution()
