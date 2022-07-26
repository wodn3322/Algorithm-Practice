def solution():
    numList = []
    for i in range(1, 10000):
        numList.append(i)
    for i in range(1, 10000):
        targetNum = i
        sum = targetNum
        while True:
            sum += targetNum % 10
            if targetNum // 10 != 0:
                targetNum = targetNum // 10
            else:
                break
        if sum in numList:
            numList.remove(sum)

    for i in numList:
        print(i)

    return


if __name__ == '__main__':
    solution()
