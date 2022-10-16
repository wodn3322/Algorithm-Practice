import sys

count = 0


def solution():
    global count
    n, s = map(int, sys.stdin.readline().strip().split())
    numList = list(map(int, sys.stdin.readline().strip().split()))
    numList.sort()

    def Backtracking(i, sum):
        global count
        if i >= n:
            return
        sum += numList[i]
        if sum == s:
            count += 1
        Backtracking(i + 1, sum)
        Backtracking(i + 1, sum - numList[i])

    Backtracking(0, 0)
    sys.stdout.write(str(count) + '\n')
    return


if __name__ == '__main__':
    solution()
