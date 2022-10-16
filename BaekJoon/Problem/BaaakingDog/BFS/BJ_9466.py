import sys

from collections import deque


def solution():
    caseNum = int(sys.stdin.readline().strip())

    answer = []

    def BFS():
        data = []
        while len(queue):
            n = queue.popleft()
            # n = queue[0]
            # del queue[0]
            if graph[n] in teamList:
                return
            data.append(n)
            if graph[data[-1]] == data[0]:
                # for d in data:
                #     visited[d] = 1
                #     teamList.append(d)
                return data
            if visited[graph[n]] == 0 and graph[n] != n:
                queue.append(graph[n])

    for _ in range(caseNum):
        studentNum = int(sys.stdin.readline().strip())
        teamList = []
        graph = [0]
        graph += list(map(int, sys.stdin.readline().strip().split(' ')))
        visited = [0] * (studentNum + 1)
        queue = deque()
        for i in range(1, studentNum + 1):
            if visited[i] == 0 and i not in teamList:
                queue.append(i)
                temp = BFS()
                if temp is not None:
                    teamList += temp
        answer.append(studentNum - len(teamList))
    for a in answer:
        print(a)

    return


if __name__ == '__main__':
    solution()
