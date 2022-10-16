import sys


def solution():
    restDay = int(sys.stdin.readline().strip())
    consultList = []
    for _ in range(restDay):
        consultList.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    dpList = [0] * (restDay + 1)

    for i in range(restDay - 1, -1, -1):
        if (i + consultList[i][0]) <= restDay:
            dpList[i] = max(dpList[i + 1], dpList[i + consultList[i][0]] + consultList[i][1])
        else:
            dpList[i] = dpList[i + 1]

    sys.stdout.write(str(dpList[0]) + '\n')

    return


if __name__ == '__main__':
    solution()
