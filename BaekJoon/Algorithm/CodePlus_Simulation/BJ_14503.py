import sys

from collections import deque


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    r, c, d = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    cleaned = [[0] * m for _ in range(n)]
    answer = 0
    # 북, 동 , 남, 서
    direction = [0, 1, 2, 3]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append([r, c, d])

    while len(queue):
        x, y, direct = map(int, queue.popleft())
        if cleaned[x][y] == 0:
            cleaned[x][y] = 1
            answer += 1
        for i in range(4):
            if direct == 0:
                direct = 3
            else:
                direct -= 1
            nx = x + dx[direct]
            ny = y + dy[direct]
            if graph[nx][ny] == 0 and cleaned[nx][ny] == 0:
                queue.append([nx, ny, direct])
                break
            if i == 3:
                if direct >= 2:
                    back = direct - 2
                else:
                    back = direct + 2
                if graph[x + dx[back]][y + dy[back]] != 1:
                    queue.append([x + dx[back], y + dy[back], direct])
                else:
                    break

    sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
