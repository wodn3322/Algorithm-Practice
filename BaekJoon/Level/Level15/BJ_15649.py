import sys


# timeout
# def solution2():
#     n, m = map(int, sys.stdin.readline().strip().split())
#     answerList = []
#     sample = []
#
#     def backtracking(n, m, status, list):
#         if len(status) == m:
#             if status not in answerList:
#                 answerList.append(status[:])
#             return
#         for i in range(1, n + 1):
#             if i not in status:
#                 status.append(i)
#                 backtracking(n, m, status, list)
#                 status.remove(status[-1])
#         return list
#
#     answerList = backtracking(n, m, sample, answerList)
#     for answer in answerList:
#         for i in range(m):
#             sys.stdout.write(str(answer[i]) + ' ')
#         sys.stdout.write('\n')
#
#     return


def solution():
    n, m = map(int, sys.stdin.readline().strip().split())
    sample = []

    def backtracking(n, m, status):
        if len(status) == m:
            for i in status:
                sys.stdout.write(str(i) + ' ')
            sys.stdout.write('\n')
            return
        for i in range(1, n + 1):
            if i not in status:
                status.append(i)
                backtracking(n, m, status)
                status.pop()

    backtracking(n, m, sample)

    return


if __name__ == '__main__':
    solution()
