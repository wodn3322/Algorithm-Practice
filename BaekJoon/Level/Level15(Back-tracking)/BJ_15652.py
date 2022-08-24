import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split())
    sample = []

    def backtracking(n, m, status):
        if len(status) == m:
            for s in status:
                sys.stdout.write(str(s) + ' ')
            sys.stdout.write('\n')
            return
        for i in range(1, n + 1):
            if len(status) == 0:
                status.append(i)
                backtracking(n, m, status)
                status.pop()
                continue
            if status[-1] <= i:
                status.append(i)
                backtracking(n, m, status)
                status.pop()
        return

    backtracking(n, m, sample)

    return


if __name__ == '__main__':
    solution()
