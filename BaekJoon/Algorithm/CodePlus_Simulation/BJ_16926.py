import sys


def solution():
    n, m, r = map(int, sys.stdin.readline().strip().split(' '))

    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    def rotate():
        rotateList = [[0] * m for _ in range(n)]

        for i in range(min(n, m) // 2):

            # 상
            for j in range(i, len(graph[0]) - 1 - i):
                rotateList[i][j] = graph[i][j + 1]
            # 하
            for j in range(i, len(graph[0]) - 1 - i):
                rotateList[len(graph) - 1 - i][j + 1] = graph[len(graph) - 1 - i][j]

            # 좌
            for j in range(i, len(graph) - 1 - i):
                rotateList[j + 1][i] = graph[j][i]

            # 우
            for j in range(i, len(graph) - 1 - i):
                rotateList[j][len(graph[0]) - 1 - i] = graph[j + 1][len(graph[0]) - 1 - i]

            # for ro in rotateList:
            #     print(ro)
            # print()

        return rotateList

    if r >= (2 * m + 2 * n - 4):
        r %= (2 * m + 2 * n - 4)

    for _ in range(r):
        graph = rotate()

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            sys.stdout.write(str(graph[i][j]) + ' ')
        sys.stdout.write('\n')

    return


if __name__ == '__main__':
    solution()
