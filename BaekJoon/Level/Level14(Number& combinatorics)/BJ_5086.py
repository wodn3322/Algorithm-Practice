import sys


def solution():
    while True:
        a, b = map(int, sys.stdin.readline().strip().split(' '))
        if a == 0 and b == 0:
            break
        if b // a > 0 and b % a == 0:
            sys.stdout.write('factor\n')
            continue
        if a // b > 0 and a % b == 0:
            sys.stdout.write('multiple\n')
            continue
        sys.stdout.write('neither\n')

    return


if __name__ == '__main__':
    solution()
