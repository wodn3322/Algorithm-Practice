import sys


def solution():
    n = int(sys.stdin.readline().strip())
    count = 0
    for i in range(1, 1 + n):
        if i < 100:
            count += 1
        else:
            numList = list(map(int, str(i)))
            if numList[0] - numList[1] == numList[1] - numList[2]:
                count += 1

    sys.stdout.write(str(count) + '\n')

    return


if __name__ == '__main__':
    solution()
