import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split())
    answerList = []
    sample = []

    def backtracking(n, m, status):
        if len(status) == m:
            if sorted(status) not in answerList:
                answerList.append(status[:])
            return
        for i in range(1, n + 1):
            if i not in status:
                status.append(i)
                backtracking(n, m, status)
                status.pop()

    backtracking(n, m, sample)

    for answer in answerList:
        for i in answer:
            sys.stdout.write(str(i) + ' ')
        sys.stdout.write('\n')

    return


if __name__ == '__main__':
    solution()
