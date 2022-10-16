import sys


# sys.stdin.readline().strip()
def solution():
    caseNum = int(sys.stdin.readline().strip())
    answer = []

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    def BFS(x, y):
        if x == endX and y == endY:
            answer.append(graph[y][x])
            return
        queue = []
        queue.append([x, y])

        while len(queue):
            nowX, nowY = map(int, queue[0])
            if nowX == endX and nowY == endY:
                answer.append(graph[endY][endX])
                return
            del queue[0]

            for i in range(8):
                nX = nowX + dx[i]
                nY = nowY + dy[i]
                if 0 <= nX < size and 0 <= nY < size:
                    if graph[nY][nX] == 0:
                        graph[nY][nX] = graph[nowY][nowX] + 1
                        queue.append([nX, nY])

    for _ in range(caseNum):
        size = int(sys.stdin.readline().strip())
        graph = [[0] * size for _ in range(size)]

        startX, startY = map(int, sys.stdin.readline().strip().split())
        endX, endY = map(int, sys.stdin.readline().strip().split())
        BFS(startX, startY)

    for a in answer:
        sys.stdout.write(str(a) + '\n')
    return


if __name__ == '__main__':
    solution()
