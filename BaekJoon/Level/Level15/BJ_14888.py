import sys


def solution():
    numCount = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().strip().split(' ')))
    add, minus, mul, divide = map(int, sys.stdin.readline().strip().split())
    totalOperCount = numCount - 1
    nowNum = numList[0]
    answerList = []

    def backtracking(num, count, a, b, c, d, calList):
        if count == 0:
            if num not in answerList:
                answerList.append(num)
            return
        else:
            if a > 0:
                backtracking(num + numList[numCount - count], count - 1, a - 1, b, c, d, calList)
            if b > 0:
                backtracking(num - numList[numCount - count], count - 1, a, b - 1, c, d, calList)
            if c > 0:
                backtracking(num * numList[numCount - count], count - 1, a, b, c - 1, d, calList)
            if d > 0:
                temp = num
                if num < 0:
                    num = -num
                    num //= numList[numCount - count]
                    num = -num
                else:
                    num //= numList[numCount - count]
                backtracking(num, count - 1, a, b, c, d - 1, calList)
                num = temp

    backtracking(nowNum, totalOperCount, add, minus, mul, divide, answerList)
    sys.stdout.write(str(max(answerList)) + '\n' + str(min(answerList)))
    return


if __name__ == '__main__':
    solution()
