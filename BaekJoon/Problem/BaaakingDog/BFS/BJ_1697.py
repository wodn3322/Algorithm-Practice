import sys


def solution():
    answer = []

    n, k = map(int, sys.stdin.readline().strip().split(' '))
    bigNum = max(n, k)
    graph = [0] * (2 * bigNum + 1)
    queue = []
    queue.append([n, 0])

    def BFS():
        while len(queue):
            loc, t = map(int, queue[0])
            del queue[0]
            if loc == k:
                answer.append(t)
                continue
            for i in range(3):
                if i == 0 and 0 <= loc - 1 <= 2 * bigNum and graph[loc - 1] == 0:
                    graph[loc - 1] = 1
                    queue.append([loc - 1, t + 1])

                if i == 1 and 0 <= loc + 1 <= 2 * bigNum and graph[loc + 1] == 0:
                    graph[loc + 1] = 1
                    queue.append([loc + 1, t + 1])

                if i == 2 and 0 <= loc * 2 <= 2 * bigNum and graph[loc * 2] == 0:
                    graph[loc * 2] = 1
                    queue.append([2 * loc, t + 1])

    BFS()

    sys.stdout.write(str(min(answer)) + '\n')

    return


if __name__ == '__main__':
    solution()
