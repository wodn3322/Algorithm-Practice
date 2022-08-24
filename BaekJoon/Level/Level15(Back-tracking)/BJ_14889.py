import sys


def solution():
    totalNum = int(sys.stdin.readline().strip())
    synergyArr = [[]] * totalNum
    totalSet = set()
    startTeam = set()
    for i in range(totalNum):
        synergyArr[i] = list(map(int, sys.stdin.readline().strip().split(' ')))
        totalSet.add(i + 1)
    answerNum = 99999

    def backtracking(minNum, nowNum, nowSet, index):
        if len(nowSet) == totalNum // 2:
            linkSet = totalSet.difference(nowSet)
            tempNum = 0
            for i in linkSet:
                for j in linkSet:
                    if i != j:
                        tempNum += synergyArr[i - 1][j - 1]
            minNum = min(minNum, abs(nowNum - tempNum))
            return minNum

        else:
            for i in range(index, totalNum):
                if i + 1 not in nowSet:
                    temp = 0
                    for s in nowSet:
                        temp += synergyArr[s - 1][i]
                        temp += synergyArr[i][s - 1]
                    nowSet.add(i + 1)
                    nowNum += temp
                    minNum = backtracking(minNum, nowNum, nowSet, i + 1)
                    nowNum -= temp
                    nowSet.remove(i + 1)

            return minNum

    answerNum = backtracking(answerNum, 0, startTeam, 0)

    sys.stdout.write(str(answerNum))
    return


if __name__ == '__main__':
    solution()
