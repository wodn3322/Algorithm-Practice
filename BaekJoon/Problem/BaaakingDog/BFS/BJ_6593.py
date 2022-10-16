import sys


def solution():
    answer = []
    dz = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]

    def BFS():
        while len(queue):
            z, x, y, t = queue[0]
            if endPoint == (z, x, y):
                return t
            del queue[0]
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                    if graph[nz][nx][ny] != '#' and visited[nz][nx][ny] == 0:
                        visited[nz][nx][ny] = 1
                        queue.append((nz, nx, ny, t + 1))
        return -1

    while True:
        queue = []

        l, r, c = map(int, sys.stdin.readline().strip().split(' '))
        if l == r == c == 0:
            break
        graph = []
        visited = [[[0] * c for _ in range(r)] for _ in range(l)]
        for i in range(l):
            layer = []
            for j in range(r):
                data = list(sys.stdin.readline().strip())
                if 'S' in data:
                    visited[i][j][data.index('S')] = 1
                    queue.append((i, j, data.index('S'), 0))
                if 'E' in data:
                    endPoint = (i, j, data.index('E'))

                layer.append(data)
            sys.stdin.readline().strip()
            graph.append(layer)

        time = BFS()

        if time != -1:
            answer.append(f'Escaped in {time} minute(s).')
        else:
            answer.append('Trapped!')

    for a in answer:
        print(a)

    return


if __name__ == '__main__':
    solution()
