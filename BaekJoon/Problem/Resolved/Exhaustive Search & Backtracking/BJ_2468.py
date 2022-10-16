import sys
import copy
from collections import deque

answer = 0
answerList = []


def solution():
    global answerList
    global answer
    num = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(num)]
    # answerList = []
    maxHeight = 0
    queue = deque()

    for i in range(num):
        graph[i] = list(map(int, sys.stdin.readline().strip().split(' ')))
        maxHeight = max(maxHeight, max(graph[i]))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def BFS(a, height, v):
        global answerList
        count = 0
        while len(queue):
            y, x = map(int, queue.popleft())
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < num and 0 <= ny < num:
                    if a[ny][nx] > height and v[ny][nx] == 0:
                        v[ny][nx] = 1
                        queue.append([ny, nx])
                        count += 1
        answerList.append(count)

    def findArea(h):
        global answer, answerList
        answerList = []
        area = copy.deepcopy(graph)
        visited = [[0] * num for _ in range(num)]
        for i in range(num):
            for j in range(num):
                if area[i][j] > h and visited[i][j] == 0:
                    queue.append([i, j])
                    BFS(area, h, visited)
                    answer = max(answer, len(answerList))

    # def findArea(h):
    #     global answer, answerList
    #     answerList = []
    #     area = copy.deepcopy(graph)
    #     for i in range(num):
    #         for j in range(num):
    #             if 0 < area[i][j] <= h:
    #                 area[i][j] = 0
    #
    #     for i in range(num):
    #         for j in range(num):
    #             if area[i][j] != 0:
    #                 queue.append([i, j])
    #                 BFS(area)
    #                 answer = max(answer, len(answerList))

    if maxHeight > 100:
        maxHeight = 100
    for i in range(maxHeight + 1):
        findArea(i)
    sys.stdout.write(str(answer) + '\n')
    return


if __name__ == '__main__':
    solution()
