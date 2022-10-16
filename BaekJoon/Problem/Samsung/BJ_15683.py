import sys

import copy

answer = 64


def solution():
    global answer
    n, m = map(int, sys.stdin.readline().strip().split(' '))

    room = []
    cctvList = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    cctvType = [
        [],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]]
    ]
    for i in range(n):
        roomInfo = list(map(int, sys.stdin.readline().strip().split(' ')))
        for j in range(m):
            if 0 < roomInfo[j] < 6:
                cctvList.append([roomInfo[j], i, j])
        room.append(roomInfo)

    def BFS(mapNow, count):
        global answer
        if count == len(cctvList):
            blindSpot = 0
            for m in mapNow:
                blindSpot += m.count(0)
            answer = min(answer, blindSpot)
            return

        cctv = cctvList[count]
        for directions in cctvType[cctv[0]]:
            copyMap = copy.deepcopy(mapNow)
            for d in directions:
                nx = cctv[1] + dx[d]
                ny = cctv[2] + dy[d]
                while 0 <= nx < len(copyMap) and 0 <= ny < len(copyMap[0]):
                    if copyMap[nx][ny] == 6:
                        break
                    if copyMap[nx][ny] == '#' or 1 <= copyMap[nx][ny] <= 5:
                        nx += dx[d]
                        ny += dy[d]
                        continue

                    if copyMap[nx][ny] == 0:
                        copyMap[nx][ny] = '#'
                        nx += dx[d]
                        ny += dy[d]

            BFS(copyMap, count + 1)

    BFS(room, 0)
    print(answer)

    return


if __name__ == '__main__':
    solution()
