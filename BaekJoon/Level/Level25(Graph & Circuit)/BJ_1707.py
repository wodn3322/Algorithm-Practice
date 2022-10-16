import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def solution():
    caseNum = int(sys.stdin.readline().strip())

    def BFS(num):
        visited[num] = 1
        queue = deque()
        queue.append(num)
        while len(queue):
            n = queue.popleft()
            for i in graph[n]:
                if visited[i] == 0:
                    visited[i] = -visited[n]
                    queue.append(i)
                else:
                    if visited[i] == visited[n]:
                        return False
        return True

    for _ in range(caseNum):
        vNUm, eNum = map(int, sys.stdin.readline().strip().split(' '))
        check = True
        graph = [[] for _ in range(vNUm + 1)]
        visited = [0] * (vNUm + 1)
        for _ in range(eNum):
            a, b = map(int, sys.stdin.readline().strip().split(' '))
            graph[a].append(b)
            graph[b].append(a)
        for i in range(1, vNUm + 1):
            if visited[i] == 0:
                if not BFS(i):
                    check = False
                    break
        if check:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')

    return


if __name__ == '__main__':
    solution()
