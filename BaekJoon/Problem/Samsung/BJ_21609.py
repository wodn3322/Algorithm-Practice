import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))

    point = 0
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))
    visited = [[0] * n for _ in range(n)]

    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFS(block, rain, color):
        blocks = []
        rainbow = []
        while len(queue):
            x, y = map(int, queue[0])
            del queue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if (graph[nx][ny] == color or graph[nx][ny] == 0) and visited[nx][ny] == 0:
                        if graph[nx][ny] == 0:
                            rainbow.append([nx, ny])
                        blocks.append([nx, ny])
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
        for r in rainbow:
            x, y = map(int, r)
            visited[x][y] = 0

        blocks.sort()
        if len(block) < len(blocks):
            block = blocks
            rain = rainbow
        elif len(block) == len((blocks)) and len(rain) <= len(rainbow):
            block = blocks
            rain = rainbow
        return block, rain

    def gravity():
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if graph[i][j] == -2:
                    for k in range(i - 1, -1, -1):
                        if graph[k][j] >= 0:
                            graph[i][j] = graph[k][j]
                            graph[k][j] = -2
                            break
                        elif graph[k][j] == -1:
                            break

    while True:
        blockList = []
        rainbowList = []
        visited = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if graph[i][j] > 0 and visited[i][j] == 0:
                    queue.append([i, j])
                    blockList, rainbowList = BFS(blockList, rainbowList, graph[i][j])
        if len(blockList) < 2:
            break
        point += len(blockList) ** 2
        for b in blockList:
            graph[b[0]][b[1]] = -2
        gravity()
        graph = list(zip(*graph))[::-1]
        graph = [list(g) for g in graph]
        gravity()
    print(point)

    return


if __name__ == '__main__':
    solution()

    # temp = list(zip(*graph))[::-1]
    # print(temp)
    # temp  = [list(s)[::] for s in temp]
    # for t in temp:
    #     print(t)
