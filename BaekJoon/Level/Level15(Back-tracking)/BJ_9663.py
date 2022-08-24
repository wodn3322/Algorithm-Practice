import sys


def solution():
    num = int(sys.stdin.readline().strip())
    location = [0] * num
    locationVisited = [0] * num
    answerCount = 0

    def checkLocation(n):
        for i in range(n):
            if location[i] == location[n] or abs(location[n] - location[i]) == n - i:
                return 0
        return 1

    def backtracking(n, countNum):
        if num == n:
            countNum += 1

            return countNum
        else:
            for i in range(num):
                if locationVisited[i]:
                    continue

                location[n] = i
                if checkLocation(n):
                    locationVisited[i] = 1
                    countNum = backtracking(n + 1, countNum)
                    locationVisited[i] = 0
        return countNum

    answerCount = backtracking(0, answerCount)

    sys.stdout.write(str(answerCount) + '\n')
    return


if __name__ == '__main__':
    solution()


    # for _ in range(num):
    #     field.append([0] * num)
    #
    # answerList = []
    #
    # queen = 2
    # canNotUse = 1
    # queenPathCount = 0
    #
    # def fillCanNotUse(x, y, field):
    #     for i in range(num):
    #         if field[i][y] != queen:
    #             field[i][y] = canNotUse
    #         if field[x][i] != queen:
    #             field[x][i] = canNotUse
    #         # if
    #
    # def rollbackCanNotUse(x, y, field):
    #     for i in range(num):
    #         if i != x:
    #             field[i][y] = 0
    #         if i != y:
    #             field[x][i] = 0
    #         # if
    #
    # def backtracking(count, inputfield, pathCount):
    #     if count == num:
    #         print('pathCount', pathCount)
    #         pathCount += 1
    #         print(pathCount)
    #         return pathCount
    #     for i in range(num):
    #         for j in range(num):
    #             if inputfield[i][j] == 0:
    #                 inputfield[i][j] = 2
    #                 count += 1
    #                 fillCanNotUse(i, j, inputfield)
    #                 print(inputfield)
    #                 pathCount =backtracking(count, inputfield, pathCount)
    #                 rollbackCanNotUse(i, j, inputfield)
    #                 print('after rollback',inputfield)
    #                 count -= 1
    #                 inputfield[i][j] = 0
    #     return pathCount
    #
    # queenPathCount= backtracking(0, field, queenPathCount)
    # print(queenPathCount)
