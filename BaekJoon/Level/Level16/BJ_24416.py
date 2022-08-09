import sys

recursiveNum = 0
dynamicNum = 0


def solution():
    targetNum = int(sys.stdin.readline().strip())

    # recurive
    def recurive(n):
        if n <= 2:
            global recursiveNum
            recursiveNum += 1
            return 1
        else:
            return recurive(n - 1) + recurive(n - 2)

    def dynamic(n):
        dynamicData = [0] * targetNum
        dynamicData[0] = 1
        dynamicData[1] = 1
        global dynamicNum
        for i in range(2, n):
            dynamicNum += 1
            dynamicData[i] = dynamicData[i - 1] + dynamicData[i - 2]
        return dynamicData[n - 1]

    recurive(targetNum)
    dynamic(targetNum)
    sys.stdout.write(str(recursiveNum) + ' ' + str(dynamicNum))

    return


if __name__ == '__main__':
    solution()
