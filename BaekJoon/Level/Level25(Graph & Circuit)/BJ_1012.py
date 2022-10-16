import sys

sys.setrecursionlimit(10 ** 6)

count = 0


def solution():
    global count
    caseNum = int(sys.stdin.readline().strip())
    caseSpecList = []
    answer = []

    def DFS(y, x):
        global count
        visited[y][x] = 1
        count += 1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph):
                if visited[ny][nx] == 0 and graph[ny][nx] == 1:
                    DFS(ny, nx)
                else:
                    continue

    for _ in range(caseNum):
        caseSpecList = list(map(int, sys.stdin.readline().strip().split(' ')))
        graph = [[0] * caseSpecList[0] for _ in range(caseSpecList[1])]
        visited = [[0] * caseSpecList[0] for _ in range(caseSpecList[1])]
        worm = []

        for _ in range(caseSpecList[2]):
            x, y = map(int, sys.stdin.readline().strip().split(' '))
            graph[y][x] = 1

        for i in range(caseSpecList[1]):
            for j in range(caseSpecList[0]):
                if visited[i][j] == 0 and graph[i][j] == 1:
                    DFS(i, j)
                    worm.append(count)
                    count = 0
        answer.append(len(worm))

    for a in answer:
        sys.stdout.write(str(a) + '\n')

    return


if __name__ == '__main__':
    solution()
