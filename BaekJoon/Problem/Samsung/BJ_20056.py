import sys

from collections import deque


def solution():
    n, m, k = map(int, sys.stdin.readline().strip().split(' '))
    queue = deque()
    graph = [[[] for _ in range(n)] for _ in range(n)]
    test = dict()
    for _ in range(m):
        # r 행, c 열, m 질량, s 속력 ,d 방
        data = list(map(int, sys.stdin.readline().strip().split(' ')))
        queue.append([data[0] - 1, data[1] - 1])
        graph[data[0] - 1][data[1] - 1].append(data[2:])
        test[(data[0], data[1])] = [data[2:]]
    dx = [- 1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for _ in range(k):
        temp = dict()
        for i in test:
            x, y = i
            for j in test[i]:
                m, s, d = map(int, j)
                nx = x + (dx[d] * s) % n
                ny = y + (dy[d] * s) % n
                if nx >= n:
                    nx = nx - n
                elif nx < 0:
                    nx = n + nx
                if ny >= n:
                    ny = ny - n
                elif ny < 0:
                    ny = n + ny
                if (nx, ny) not in temp:
                    temp[(nx, ny)] = [[m, s, d]]
                else:
                    temp[(nx, ny)].append([m, s, d])

        test = temp
        for i in test:
            dataList = []
            if len(test[i]) > 1:
                directCheck = []
                sameDirect = [0, 2, 4, 6]
                diffDirect = [1, 3, 5, 7]
                sumM = 0
                sumV = 0
                for d in test[i]:
                    sumM += d[0]
                    sumV += d[1]
                    directCheck.append(d[2] % 2)
                if sumM // 5 != 0:
                    if directCheck.count(0) == len(test[i]) or directCheck.count(1) == len(test[i]):
                        for j in sameDirect:
                            dataList.append([sumM // 5, sumV // len(test[i]), j])
                    else:
                        for j in diffDirect:
                            dataList.append([sumM // 5, sumV // len(test[i]), j])
                test[i] = dataList
    totalM = 0
    for i in test:
        for data in test[i]:
            totalM += data[0]
    print(totalM)

    # for _ in range(k):
    #     for _ in range(len(queue)):
    #         x, y = map(int, queue.popleft())
    #         # x, y = map(int, queue[0])
    #         # del queue[0]
    #         data = graph[x][y][0]
    #         nx = x + (dx[data[2]] * data[1]) % n
    #         if nx >= n:
    #             nx = nx - n
    #         elif nx < 0:
    #             nx = n + nx
    #         ny = y + (dy[data[2]] * data[1]) % n
    #         if ny >= n:
    #             ny = ny - n
    #         elif ny < 0:
    #             ny = n + ny
    #         queue.append([nx, ny])
    #         del graph[x][y][0]
    #         graph[nx][ny].append(data)
    #
    #     removeList = deque()
    #     newQueue = deque()
    #     while len(queue):
    #         x, y = map(int, queue.popleft())
    #         # x, y = map(int, queue[0])
    #         # del queue[0]
    #         if len(graph[x][y]) > 1:
    #             if [x, y] in removeList:
    #                 continue
    #             else:
    #                 removeList.append([x, y])
    #                 checkDirect = []
    #                 stackSum = 0
    #                 stackV = 0
    #                 fireBallNum = len(graph[x][y])
    #                 for g in graph[x][y]:
    #                     stackSum += g[0]
    #                     stackV += g[1]
    #                     checkDirect.append(g[2] % 2)
    #                 if checkDirect.count(0) == len(graph[x][y]) or checkDirect.count(1) == len(graph[x][y]):
    #                     directList = [0, 2, 4, 6]
    #                 else:
    #                     directList = [1, 3, 5, 7]
    #
    #                 for i in directList:
    #                     sumNum = stackSum // 5
    #                     if sumNum != 0:
    #                         newQueue.append([x, y])
    #                         graph[x][y].append([sumNum, stackV // fireBallNum, i])
    #
    #                 for _ in range(fireBallNum):
    #                     del graph[x][y][0]
    #
    #         else:
    #             if [x, y] not in removeList:
    #                 newQueue.append([x, y])
    #     while len(newQueue):
    #         queue.append(newQueue.popleft())
    #
    # mSum = 0
    # while (queue):
    #     x, y = map(int, queue[0])
    #     del queue[0]
    #     mSum += graph[x][y][0][0]
    # print(mSum)
    return


if __name__ == '__main__':
    solution()
