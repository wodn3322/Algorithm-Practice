import sys

sys.setrecursionlimit(10 ** 3)
answer = 0
answerList = []


def solution():
    global answer, answerList
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    graph = [[] for _ in range(n)]
    aptList = []
    chiList = []
    nowList = []
    for i in range(n):
        graph[i] = list(map(int, sys.stdin.readline().strip().split(' ')))
        for j in range(n):
            if graph[i][j] == 2:
                chiList.append([i, j])
            elif graph[i][j] == 1:
                aptList.append([i, j])

    def calDistance():
        global answer
        answer = 0
        dis = 0
        for a in aptList:
            disList = []
            for now in nowList:
                disList.append(abs(now[0] - a[0]) + abs(now[1] - a[1]))
            answer += min(disList)
        answerList.append(answer)

    def BackTracking(i):
        if len(nowList) >= m:
            calDistance()
        if i == len(chiList):
            return

        if len(nowList) < m:
            nowList.append(chiList[i])
            BackTracking(i + 1)
            nowList.pop()
            BackTracking(i + 1)

    BackTracking(0)

    sys.stdout.write(str(min(answerList)) + '\n')

    return


if __name__ == '__main__':
    solution()
