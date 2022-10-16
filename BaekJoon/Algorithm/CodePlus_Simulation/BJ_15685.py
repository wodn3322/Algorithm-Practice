import sys


def solution():
    caseNum = int(sys.stdin.readline().strip())
    answer = 0
    dotList = []
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    curveList = []

    for _ in range(caseNum):
        curveList.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    for curve in curveList:
        nowDots = []
        nowDots.append(([curve[0], curve[1]]))
        nowDots.append(([curve[0] + dx[curve[2]], curve[1] + dy[curve[2]]]))
        directionList = []
        directionList.append(curve[2])
        for i in range(curve[3]):
            reverseDirect = directionList[::-1]
            for r in reverseDirect:
                if r == 3:
                    r = 0
                else:
                    r += 1
                nowDots.append([nowDots[-1][0] + dx[r], nowDots[-1][1] + dy[r]])
                directionList.append(r)
        for n in nowDots:
            if n not in dotList:
                dotList.append(n)

    for d in dotList:
        check = True
        x, y = d[0], d[1]
        for i in range(4):
            x += dx[i]
            y += dy[i]
            if [x, y] in dotList:
                continue
            else:
                check = False
                break
        if check:
            answer += 1

    print(answer)

    return


if __name__ == '__main__':
    solution()
