import sys


def solution():
    n = int(sys.stdin.readline().strip())
    answer = []
    graph = []
    visited = [[0] * n for _ in range(n)]

    queue = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(n):
        graph.append(list(map(int, list(sys.stdin.readline().strip()))))

    def BFS():
        count = 1
        while len(queue):
            x, y = map(int, queue[0])
            del queue[0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        count += 1
                        queue.append([nx, ny])
        answer.append(count)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                queue.append([i, j])
                BFS()

    answer.sort()
    print(len(answer))
    for a in answer:
        print(a)

    return


if __name__ == '__main__':
    solution()
