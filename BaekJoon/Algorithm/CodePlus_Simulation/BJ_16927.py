import sys

from collections import deque

# https://maeng2world.tistory.com/197 <- 보고 다시 풀기

def solution():
    n, m, r = map(int, sys.stdin.readline().strip().split(' '))
    queue = deque()
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    def rotate():
        for i in range(min(n, m) // 2):
            # 상
            for j in range(i, m - i):
                queue.append(graph[i][j])
            # 우
            for j in range(i + 1, n - 1 - i):
                queue.append(graph[j][m - 1 - i])
            # 하
            for j in range(m - i - 1, i - 1, -1):
                queue.append(graph[n - 1 - i][j])
            # 좌
            for j in range(n - 2 - i, i, -1):
                queue.append(graph[j][i])

            queue.rotate(-r)

            for j in range(i, m - i):
                graph[i][j] = queue.popleft()
            # 우
            for j in range(i + 1, n - 1 - i):
                graph[j][len(graph[0]) - 1 - i] = queue.popleft()
            # 하
            for j in range(m - i - 1, i - 1, -1):
                graph[len(graph) - 1 - i][j] = queue.popleft()
            # 좌
            for j in range(n - 2 - i, i, -1):
                graph[j][i] = queue.popleft()

    if r >= (2 * m + 2 * n - 4):
        r %= (2 * m + 2 * n - 4)

    rotate()

    for i in range(n):
        for j in range(m):
            sys.stdout.write(str(graph[i][j]) + ' ')
        sys.stdout.write('\n')

    return


if __name__ == '__main__':
    solution()
