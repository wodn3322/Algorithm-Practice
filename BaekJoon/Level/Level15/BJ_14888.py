import sys


def solution():
    numCount = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().strip().split(' ')))
    add, minus, mul, divide = map(int, sys.stdin.readline().strip().split())
    totalOperCount = numCount - 1
    nowNum = numList[0]
    maxNum = -1000000000
    minNum = 1000000000

    def backtracking(num, count, a, b, c, d, maxN, minN):
        print(maxN,minN)
        if count == 0:
            sys.stdout.write(str(maxN) + '\n' + str(minN) + '\n')
            exit()
        else:
            if a > 0:
                num += numList[numCount - count]
                count -= 1
                maxN = max(num, maxN)
                minN = min(num, minN)
                backtracking(num, count, a - 1, b, c, d, maxN, minN)
            if b > 0:
                num -= numList[numCount - count]
                count -= 1
                maxN = max(num, maxN)
                minN = min(num, minN)
                backtracking(num, count, a, b - 1, c, d, maxN, minN)
            if c > 0:
                num *= numList[numCount - count]
                count -= 1
                maxN = max(num, maxN)
                minN = min(num, minN)
                backtracking(num, count, a, b, c - 1, d, maxN, minN)
            if d > 0:
                num //= numList[numCount - count]
                count -= 1
                maxN = max(num, maxN)
                minN = min(num, minN)
                backtracking(num, count, a, b, c, d - 1, maxN, minN)

    backtracking(nowNum, totalOperCount, add, minus, mul, divide, maxNum, minNum)

    return


if __name__ == '__main__':
    solution()
