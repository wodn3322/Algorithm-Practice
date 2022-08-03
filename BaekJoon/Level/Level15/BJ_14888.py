import sys


def solution():
    numCount = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().strip().split(' ')))
    add, minus, mul, divide = map(int, sys.stdin.readline().strip().split())
    totalOperCount = numCount - 1
    nowNum = numList[0]
    answerList = []
    maxNum = -1000000000
    minNum = 1000000000

    def backtracking(num, count, a, b, c, d, calList):
        # print(num, count, a, b, c, d)
        if count == 0:
            # # print('befor append',num)
            if num not in answerList:
                answerList.append(num)
            # calList.append(num)
            return
            # sys.stdout.write(str(max(calList)) + '\n' + str(min(calList)) + '\n')
            # return max(calList), min(calList)
        else:
            if a > 0:
                # num += numList[numCount - count]
                # count -= 1
                # maxN = max(num, maxN)
                # minN = min(num, minN)
                # backtracking(num + numList[numCount - count], count-1, a - 1, b, c, d, max(num, maxN), min(num, minN))
                backtracking(num + numList[numCount - count], count - 1, a - 1, b, c, d, calList)
                # minN = max(num, minN)
                # maxN = min(num, maxN)
                # count += 1
                # num -= numList[numCount - count]
            if b > 0:
                # num -= numList[numCount - count]
                backtracking(num - numList[numCount - count], count - 1, a, b - 1, c, d, calList)
                # num += numList[numCount - count]
            if c > 0:
                # num *= numList[numCount - count]
                # maxN = max(num, maxN)
                # minN = min(num, minN)
                backtracking(num * numList[numCount - count], count - 1, a, b, c - 1, d, calList)
                # minN = max(num, minN)
                # maxN = min(num, maxN)
                # num //= numList[numCount - count]

            if d > 0:
                temp = num
                if num < 0:
                    num = -num
                    num //= numList[numCount - count]
                    num = -num
                else:
                    num //= numList[numCount - count]
                # count -= 1
                # backtracking(num // numList[numCount - count], count-1, a, b, c, d - 1, max(num, maxN), min(num, minN))
                backtracking(num, count - 1, a, b, c, d - 1, calList)
                # minN = max(num, minN)
                # maxN = min(num, maxN)
                # count += 1
                num = temp

    # print(backtracking(nowNum, totalOperCount, add, minus, mul, divide, maxNum, minNum))
    backtracking(nowNum, totalOperCount, add, minus, mul, divide, answerList)
    # print(max(answerList), '\n', min(answerList))
    sys.stdout.write(str(max(answerList)) + '\n' + str(min(answerList)))
    return


if __name__ == '__main__':
    solution()
