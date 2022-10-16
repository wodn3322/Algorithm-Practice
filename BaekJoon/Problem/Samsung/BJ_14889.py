import sys

answer = 40000


def solution():
    global answer
    size = int(sys.stdin.readline().strip())

    graph = []

    for _ in range(size):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    visited = [0] * size

    def DFS(count, index):
        global answer
        if count != size // 2:
            for i in range(index, size):
                visited[i] = 1
                DFS(count + 1, i + 1)
                visited[i] = 0
        else:
            sumNUm = 0
            for i in range(size):
                for j in range(i + 1, size):
                    if visited[i] == 1 and visited[j] == 1:
                        sumNUm += (graph[i][j] + graph[j][i])
                    elif visited[i] == 0 and visited[j] == 0:
                        sumNUm -= (graph[i][j] + graph[j][i])
            answer = min(answer, abs(sumNUm))
        return

    DFS(0, 0)

    # teamList = []
    #
    # def DFS(lastIndex):
    #     global answer
    #     if len(teamList) != size // 2:
    #         for i in range(lastIndex + 1, size):
    #             if i not in teamList:
    #                 teamList.append(i)
    #                 DFS(i)
    #                 teamList.pop()
    #     else:
    #         sumNum = 0
    #         for i in range(size):
    #             for j in range(size):
    #                 if i in teamList and j in teamList:
    #                     sumNum += graph[i][j]
    #                 elif i not in teamList and j not in teamList:
    #                     sumNum -= graph[i][j]
    #         answer = min(answer, abs(sumNum))
    #
    # DFS(0)
    sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
