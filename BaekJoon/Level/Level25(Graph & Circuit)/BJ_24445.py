import sys

sys.setrecursionlimit(10 ** 6)

count = 1


def solution():
    vNum, eNum, start = map(int, sys.stdin.readline().strip().split(' '))
    answer = [0] * (vNum + 1)
    graph = [[] for _ in range(vNum + 1)]
    visited = [0] * (vNum + 1)
    visitQueue = []
    for _ in range(eNum):
        x, y = map(int, sys.stdin.readline().strip().split(' '))
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, vNum + 1):
        graph[i].sort(reverse=True)
    visited[start] = 1
    visitQueue.append(start)
    answer[start] = count

    def BFS():
        global count
        while len(visitQueue):
            top = visitQueue[0]
            visitQueue.remove(top)
            for i in graph[top]:
                if visited[i]==0:
                    count+=1
                    answer[i] = count
                    visited[i] =1
                    visitQueue.append(i)

    BFS()

    for i in range(1, vNum + 1):
        sys.stdout.write(str(answer[i]) + '\n')

    return


if __name__ == '__main__':
    solution()
