import sys


def solution():
    roomNum = int(sys.stdin.readline().strip())
    roomStatus = list(map(int, sys.stdin.readline().strip().split(' ')))
    mainDirect, subDirect = map(int, sys.stdin.readline().strip().split(' '))

    directNum = 0

    for status in roomStatus:
        directNum += 1
        status -= mainDirect
        if status > 0:
            directNum += (status // subDirect)
            if status % subDirect != 0:
                directNum += 1

    sys.stdout.write(str(directNum) + '\n')

    return


if __name__ == '__main__':
    solution()
