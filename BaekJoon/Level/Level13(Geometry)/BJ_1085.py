import sys


def solution():
    x, y, w, h = map(int, sys.stdin.readline().strip().split())
    lengthList = []
    lengthList.append(abs(w - x))
    lengthList.append(abs(0 - x))
    lengthList.append(abs(h - y))
    lengthList.append(abs(0 - y))
    sys.stdout.write(str(min(lengthList)) + '\n')

    return


if __name__ == '__main__':
    solution()
