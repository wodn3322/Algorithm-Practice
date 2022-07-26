import sys


def solution():
    aNum, bNum = map(int, sys.stdin.readline().strip().split())
    aSet = set(map(int, sys.stdin.readline().strip().split(' ')))
    bSet = set(map(int, sys.stdin.readline().strip().split(' ')))
    totalSet = aSet.union(bSet) - aSet.intersection(bSet)
    print(len(totalSet))

    return


if __name__ == '__main__':
    solution()
