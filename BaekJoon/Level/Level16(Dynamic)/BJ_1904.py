import sys


def solution():
    nNum = int(sys.stdin.readline().strip())

    data = [0 for _ in range(nNum + 1)]
    data[0] = 1
    data[1] = 2
    for i in range(2, nNum):
        data[i] = (data[i - 1] + data[i - 2]) % 15746
    sys.stdout.write(str(data[nNum - 1]) + '\n')

    return


if __name__ == '__main__':
    solution()
