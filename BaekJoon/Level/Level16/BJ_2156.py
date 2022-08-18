import sys


def solution():
    juiceNum = int(sys.stdin.readline().strip())
    juiceList = [0] * juiceNum

    for i in range(juiceNum):
        juiceList[i] = int(sys.stdin.readline().strip())

    dynamicList = [0] * (juiceNum + 1)
    if juiceNum>=1:
        dynamicList[1] = juiceList[0]
    if juiceNum>=2:
        dynamicList[2] = max(dynamicList[1],juiceList[1]+juiceList[0],juiceList[1])

    for i in range(3, juiceNum+1):
        dynamicList[i] = max(dynamicList[i - 1], juiceList[i - 1] + juiceList[i - 2] + dynamicList[i - 3], juiceList[i - 1] + dynamicList[i - 2])
    sys.stdout.write(str(max(dynamicList))+'\n')

    return


if __name__ == '__main__':
    solution()
