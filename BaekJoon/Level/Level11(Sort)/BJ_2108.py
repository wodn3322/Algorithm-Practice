import sys


def solution():
    count = int(sys.stdin.readline())

    numList = []
    numCountList = [0] * 8001
    for _ in range(count):
        num = int(sys.stdin.readline())
        numList.append(num)
        numCountList[num + 4000] += 1

    # 산술평균
    sys.stdout.write(str(round(sum(numList) / len((numList)))) + '\n')
    # 중앙값
    temp = sorted(numList)
    sys.stdout.write(str(temp[len(numList) // 2]) + '\n')
    # 최빈값
    if numCountList.count(max(numCountList)) > 1:
        mode = []
        for i in list(set(numList)):
            if numList.count(i) == max(numCountList):
                mode.append(i)
        mode.sort()
        print(mode[1])
    else:
        print(numCountList.index(max(numCountList)) - 4000)

    # 최대 최소 차이
    sys.stdout.write(str(abs(max(numList) - min(numList))))

    return


if __name__ == '__main__':
    solution()
