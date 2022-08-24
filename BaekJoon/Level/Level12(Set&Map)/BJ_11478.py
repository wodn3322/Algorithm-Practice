import sys


def solution():
    inputString = sys.stdin.readline().strip()
    partSet = set()

    for i in range(1, len(inputString) + 1):
        for j in range(len((inputString)) - i + 1):
            partSet.add(inputString[j:i + j])

    sys.stdout.write(str(len(partSet)))

    return


if __name__ == '__main__':
    solution()
