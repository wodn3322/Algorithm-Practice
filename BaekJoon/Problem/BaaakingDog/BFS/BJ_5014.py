import sys

sys.setrecursionlimit(10 ** 6)


def solution():
    f, s, g, u, d = map(int, sys.stdin.readline().strip().split(' '))
    answer = 0
    queue = []
    visited = [0] * (f + 1)
    queue.append([s, 0])

    def BFS():
        while len(queue):
            loc, count = map(int, queue[0])
            del queue[0]
            if loc == g:
                return count
            if loc + u <= f and visited[loc + u] == 0:
                queue.append([loc + u, count + 1])
                visited[loc + u] = 1
            if 1 <= loc - d and visited[loc - d] == 0:
                queue.append([loc - d, count + 1])
                visited[loc - d] = 1
        return 'use the stairs'

    answer = BFS()
    print(answer)

    return


if __name__ == '__main__':
    solution()
