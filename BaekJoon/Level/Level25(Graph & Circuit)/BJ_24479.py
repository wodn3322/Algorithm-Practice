import sys

sys.setrecursionlimit(10 ** 6)

count = 1


def solution():
    vNum, eNum, start = map(int, sys.stdin.readline().strip().split(' '))
    answer = [0] * (vNum + 1)
    graph = [[] for _ in range(vNum + 1)]
    visited = [0] * (vNum + 1)
    for _ in range(eNum):
        x, y = map(int, sys.stdin.readline().strip().split(' '))
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, vNum + 1):
        graph[i].sort()
    visited[start] = 1
    answer[start] = 1
    now = start

    def DFS(g, v, location):
        global count
        for i in g[location]:
            if v[i] == 0:
                v[i] = 1
                location = i
                count += 1
                answer[i] = count
                DFS(g, v, location)

    DFS(graph, visited, now)

    for i in range(1, vNum + 1):
        sys.stdout.write(str(answer[i]) + '\n')

    return


if __name__ == '__main__':
    solution()
