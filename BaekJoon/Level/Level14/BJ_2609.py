import sys


def solution():
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    aSet = set()
    bSet = set()

    for i in range(1, round(a ** (1 / 2)) + 1):
        if a // i >= 1 and a % i == 0:
            aSet.add(i)
            aSet.add(a / i)
    for i in range(1, round(b ** (1 / 2)) + 1):
        if b // i >= 1 and b % i == 0:
            bSet.add(i)
            bSet.add(b / i)
    abSet = aSet.intersection(bSet)
    greatest = int(max(abSet))
    smallest = int(a * b / greatest)
    sys.stdout.write(str(greatest) + '\n' + str(smallest) + '\n')

    return


if __name__ == '__main__':
    solution()
