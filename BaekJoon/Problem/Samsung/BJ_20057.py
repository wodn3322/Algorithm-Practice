import sys

outSand = 0


def solution():
    global outSand
    n = int(sys.stdin.readline().strip())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    sandPercent = [0.01, 0.01, 0.02, 0.02, 0.05, 0.07, 0.07, 0.1, 0.1]
    sandXLoc = [
        [-1, 1, -2, 2, 0, -1, 1, -1, 1],
        [0, 0, 1, 1, 3, 1, 1, 2, 2],
        [1, -1, 2, -2, 0, 1, -1, 1, -1],
        [0, 0, -1, -1, -3, -1, -1, -2, -2]
    ]
    sandYLoc = [
        [0, 0, -1, -1, -3, -1, -1, -2, -2],
        [-1, 1, -2, 2, 0, -1, 1, -1, 1],
        [0, 0, 1, 1, 3, 1, 1, 2, 2],
        [1, -1, 2, -2, 0, 1, -1, 1, -1],
    ]

    x, y = n // 2, n // 2
    loopCount = 0
    direct = 0
    length = 1

    def movdSand(d):
        global outSand
        removeSand = 0
        for i in range(len(sandPercent)):
            nx = x + sandXLoc[d][i]
            ny = y + sandYLoc[d][i]
            if 0 <= nx < n and 0 <= ny < n:
                graph[x + sandXLoc[d][i]][y + sandYLoc[d][i]] += int(graph[x + dx[d]][y + dy[d]] * sandPercent[i])
            else:
                outSand += int(graph[x + dx[d]][y + dy[d]] * sandPercent[i])
            removeSand += int(graph[x + dx[d]][y + dy[d]] * sandPercent[i])
        if 0 <= (x + dx[d] * 2) < n and 0 <= (y + dy[d] * 2) < n:
            graph[x + dx[d] * 2][y + dy[d] * 2] += (graph[x + dx[d]][y + dy[d]] - removeSand)
        else:
            outSand += (graph[x + dx[d]][y + dy[d]] - removeSand)
        graph[x + dx[d]][y + dy[d]] = 0

    while x != 0 or y != 0:
        if loopCount == 2:
            loopCount = 0
            length += 1
        else:
            for _ in range(length):
                movdSand(direct)
                x += dx[direct]
                y += dy[direct]
                if x == 0 and y == 0:
                    break
            direct = (direct + 1) % 4
            loopCount += 1

    print(outSand)
    return


if __name__ == '__main__':
    solution()
