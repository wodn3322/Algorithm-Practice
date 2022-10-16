import sys


def solution():
    num = int(sys.stdin.readline().strip())
    answer = 0
    for i in range(1, 1000001):
        nList = list(map(int, str(i)))
        if num == sum(nList) + i:
            answer = i
            break
    sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
