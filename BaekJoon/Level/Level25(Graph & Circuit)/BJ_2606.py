import sys

count = 0


def solution():
    vNUm = int(sys.stdin.readline().strip())
    eNum = int(sys.stdin.readline().strip())

    graph = [[] for _ in range(vNUm + 1)]
    visited = [0] * (vNUm + 1)
    for _ in range(eNum):
        x, y = map(int, sys.stdin.readline().strip().split(' '))
        graph[x].append(y)
        graph[y].append(x)

    target = 1
    visited[target] = 1

    def DFS(location):
        global count

        for i in graph[location]:
            if visited[i] == 0:
                visited[i] = 1
                count += 1
                DFS(i)

    DFS(target)
    sys.stdout.write(str(count) + '\n')

    return


if __name__ == '__main__':
    solution()
