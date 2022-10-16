import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def solution():
    graph = [0] * 101
    visited = [0] * 101
    ladderNum, snakeNum = map(int, sys.stdin.readline().strip().split(' '))
    ladderList = {}
    snakeList = {}
    queue = deque()

    for _ in range(ladderNum):
        s, e = map(int, sys.stdin.readline().strip().split(' '))
        ladderList[s] = e
    for _ in range(snakeNum):
        s, e = map(int, sys.stdin.readline().strip().split(' '))
        snakeList[s] = e

    queue.append(1)
    visited[1] = 1

    def BFS():
        while len(queue):
            x = queue.popleft()
            if x == 100:
                return

            for i in range(1, 7):
                nx = x + i
                if nx <= 100 :
                    if nx in ladderList:
                        nx = ladderList[nx]
                    if nx in snakeList:
                        nx = snakeList[nx]
                    if visited[nx] ==0:
                        graph[nx] = graph[x] + 1
                        visited[nx] = 1
                        queue.append(nx)

    BFS()
    sys.stdout.write(str(graph[100]) + '\n')
    return


if __name__ == '__main__':
    solution()
