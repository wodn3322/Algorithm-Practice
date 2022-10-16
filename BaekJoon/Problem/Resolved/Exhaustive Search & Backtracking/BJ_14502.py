import sys
import copy
from collections import deque

answer = 0


def solution():
    global answer
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    def BFS():
        global answer
        queue = deque()
        count = 0
        useMap = copy.deepcopy(graph)
        for i in range(n):
            for j in range(m):
                if useMap[i][j] == 2:
                    queue.append([i, j])

        while len(queue):
            y, x = map(int, queue.popleft())
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if useMap[ny][nx] == 0:
                        useMap[ny][nx] = 2
                        queue.append([ny, nx])
        for u in useMap:
            count += u.count(0)
        answer = max(answer, count)

    def walls(wallNum):
        if wallNum == 3:
            BFS()
            return
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    walls(wallNum + 1)
                    graph[i][j] = 0

    walls(0)
    sys.stdout.write(str(answer) + '\n')
    return


if __name__ == '__main__':
    solution()
