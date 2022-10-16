import sys


def solution():
    num = int(sys.stdin.readline().strip())
    count = 0
    startNum = 666

    while True:

        if '666' in str(startNum):
            count += 1
        if count == num:
            break
        startNum += 1
    sys.stdout.write(str(startNum) + '\n')

    return


if __name__ == '__main__':
    solution()
