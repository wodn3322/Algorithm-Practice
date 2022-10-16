import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    r, c, d = map(int, sys.stdin.readline().strip().split(' '))
    # d 0 - 북 , 1 - 동 , 2 - 남 , 3 - 서
    visited = [[0] * m for _ in range(n)]
    dList = [3, 2, 1, 0]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    def BFS():

    return


if __name__ == '__main__':
    solution()
