import sys


def solution():
    vNum, eNum, start = map(int, sys.stdin.readline().strip().split(' '))

    graph = [[] for _ in range(vNum + 1)]
    answerDFS = []
    answerBFS = []

    for _ in range(eNum):
        x, y = map(int, sys.stdin.readline().strip().split(' '))
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1,vNum+1):
        graph[i].sort()

    visitedDFS = [0] * (vNum + 1)
    visitedDFS[start] = 1
    answerDFS.append(start)

    def DFS(location):
        for i in graph[location]:
            if visitedDFS[i] == 0:
                visitedDFS[i] = 1
                answerDFS.append(i)
                DFS(i)

    visitedBFS = [0] * (vNum + 1)
    visitedBFS[start] = 1
    answerBFS.append(start)

    bfsQueue = []
    bfsQueue.append(start)

    def BFS():
        while len(bfsQueue):
            top = bfsQueue[0]
            bfsQueue.remove(top)
            for i in graph[top]:
                if visitedBFS[i] == 0:
                    answerBFS.append(i)
                    visitedBFS[i] = 1
                    bfsQueue.append(i)

    DFS(start)
    BFS()

    for i in range(len(answerDFS)):
        sys.stdout.write(str(answerDFS[i]) + ' ')

    sys.stdout.write('\n')

    for i in range(len(answerBFS)):
        sys.stdout.write(str(answerBFS[i]) + ' ')

    return


if __name__ == '__main__':
    solution()
