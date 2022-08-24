def solution():
    inputNum = int(input())
    startTotal = 2
    loopCheck = 1
    while True:
        inputNum -= loopCheck
        if inputNum <= 0:
            break
        loopCheck += 1
        startTotal += 1
    if loopCheck % 2 == 1:
        print(str(startTotal - (loopCheck - abs(inputNum - 1) + 1)) + "/" + str(loopCheck - abs(inputNum - 1) + 1))
    else:
        print(str(loopCheck - abs(inputNum - 1) + 1) + "/" + str(startTotal - (loopCheck - abs(inputNum - 1) + 1)))

    return


if __name__ == '__main__':
    solution()
