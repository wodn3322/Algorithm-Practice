def solution():
    num = int(input())
    totalCount = 0
    for i in range(1, num + 1):
        if i < 100:
            totalCount += 1
        else:
            numSplit = list(map(int, str(i)))
            diff = -999
            for index in range(len(numSplit) - 1):
                if index == 0:
                    diff = numSplit[index] - numSplit[index + 1]
                else:
                    if diff != numSplit[index] - numSplit[index + 1]:
                        break
                if index == len(numSplit) - 2:
                    totalCount += 1

    print(totalCount)
    return


if __name__ == '__main__':
    solution()
