import sys

babyShark = 2


def solution():
    n = int(sys.stdin.readline().strip())
    answer = []
    graph = []
    bX, bY = 0, 0
    fishList = []
    for i in range(n):
        data = list(map(int, sys.stdin.readline().strip().split(' ')))
        for d in data:
            if 1 <= d <= 6:
                fishList.append(d)
            if d == 9:
                bX, bY = i, data.index(9)
        graph.append(data)

    queue = []
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    def checkContinue(size):
        check = True
        if len(fishList) == 0:
            return False
        elif len(fishList) > 0:
            for f in fishList:
                if size > f:
                    return True
            check = False
        return check

    def BFS():
        while len(queue):
            print(fishList)
            x, y, time, sharkSize, eat = map(int, queue[0])
            del queue[0]
            if checkContinue(sharkSize):
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if 0 <= graph[nx][ny] < sharkSize:
                            if graph[nx][ny] != 0:
                                fishList.remove(graph[nx][ny])
                                graph[nx][ny] = 0
                                if eat + 1 == sharkSize:
                                    queue.append([nx, ny, time + 1, sharkSize + 1, 0])
                                else:
                                    queue.append([nx, ny, time + 1, sharkSize, eat + 1])
                            else:
                                queue.append([nx, ny, time + 1, sharkSize, eat])
            else:
                answer.append(time)

    # x,y,움직인 시간, 상어크기, 먹은 마리수
    queue.append([bX, bY, 0, 2, 0])
    BFS()
    print(min(answer))
    return


if __name__ == '__main__':
    solution()
