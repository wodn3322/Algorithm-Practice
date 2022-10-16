import sys

sys.setrecursionlimit(10 ** 6)


def solution():
    n, k = map(int, sys.stdin.readline().strip().split(' '))
    graph = [0] * 100001

    def BFS(loc):

        queue = []
        queue.append(loc)

        while queue:
            now = queue[0]
            del queue[0]
            if now == k:
                break
            for i in [now - 1, now + 1, now * 2]:
                if 0 <= i <= 100000 and graph[i] == 0:
                    graph[i] = graph[now] + 1
                    queue.append(i)

    BFS(n)
    sys.stdout.write(str(graph[k]) + '\n')
    return


if __name__ == '__main__':
    solution()
