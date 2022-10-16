import sys


def solution():
    n, m, r = map(int, sys.stdin.readline().strip().split(' '))

    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    calList = list(map(int, sys.stdin.readline().strip().split(' ')))

    def cal(num):
        if num == 1:
            rotate = [[0] * len(graph[0]) for _ in range(len(graph))]
            for i in range(len(graph) // 2):
                rotate[i] = graph[len(graph) - 1 - i]
                rotate[len(graph) - 1 - i] = graph[i]

        elif num == 2:
            rotate = [[0] * len(graph[0]) for _ in range(len(graph))]

            for i in range(len(rotate)):
                for j in range(len(rotate[0]) // 2):
                    rotate[i][j] = graph[i][len(graph[0]) - 1 - j]
                    rotate[i][len(graph[0]) - 1 - j] = graph[i][j]

        elif num == 3:
            rotate = [[0] * len(graph) for _ in range(len(graph[0]))]
            for i in range(len(graph)):
                for j in range(len(graph[0])):
                    rotate[j][len(graph) - 1 - i] = graph[i][j]

        elif num == 4:
            rotate = [[0] * len(graph) for _ in range(len(graph[0]))]

            for i in range(len(graph)):
                for j in range(len(graph[0])):
                    rotate[len(graph[0]) - 1 - j][i] = graph[i][j]

        elif num == 5:
            rotate = [[0] * len(graph[0]) for _ in range(len(graph))]

            for i in range(len(graph) // 2):
                for j in range(len(graph[0]) // 2):
                    rotate[i][j] = graph[i + len(graph) // 2][j]
                    rotate[i][j + len(graph[0]) // 2] = graph[i][j]
                    rotate[i + len(graph) // 2][j + len(graph[0]) // 2] = graph[i][j + len(graph[0]) // 2]
                    rotate[i + len(graph) // 2][j] = graph[i + len(graph) // 2][j + len(graph[0]) // 2]

        elif num == 6:
            rotate = [[0] * len(graph[0]) for _ in range(len(graph))]
            for i in range(len(graph) // 2):
                for j in range(len(graph[0]) // 2):
                    rotate[i][j] = graph[i][j + len(graph[0]) // 2]
                    rotate[i][j + len(graph[0]) // 2] = graph[i + len(graph) // 2][j + len(graph[0]) // 2]
                    rotate[i + len(graph) // 2][j + len(graph[0]) // 2] = graph[i + len(graph) // 2][j]
                    rotate[i + len(graph) // 2][j] = graph[i][j]

        return rotate

    for c in calList:
        # print(c)
        graph = cal(c)
        # for g in graph:
        #     print(g)
        # print()

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            sys.stdout.write(str(graph[i][j]) + ' ')
        sys.stdout.write('\n')

    return


if __name__ == '__main__':
    solution()
