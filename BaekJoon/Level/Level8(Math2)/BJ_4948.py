def solution():
    inputList = []
    primeList = []
    while True:
        inputList.append(int(input()))
        if inputList[-1] == 0:
            break

    for i in range(1, 123456 * 2 + 1):
        checkDivide = True
        for prime in range(2, round(i ** (1 / 2)) + 1):
            if i % prime == 0:
                checkDivide = False
                break
        if checkDivide:
            primeList.append(i)

    for i in inputList:
        if i == 0:
            return
        primeCount = 0
        for num in primeList:
            if i < num <= 2 * i:
                primeCount += 1
            if num > 2 * i:
                break
        print(primeCount)

    return


if __name__ == '__main__':
    solution()

    # 시간초과 풀이
    # num의 범위를 다시 찾는게 시간을 너무 많이 씀

    # import sys
    # inputList = []
    # primeList = []
    # while True:
    #     inputList.append(int(sys.stdin.readline()))
    #     if inputList[-1] == 0:
    #         break
    #
    # for i in range(len(inputList)):
    #     rangeNum = inputList[i]
    #     primeCount = 0
    #     if rangeNum == 0:
    #         return
    #     for num in range(rangeNum + 1, rangeNum * 2 + 1):
    #         if (num % 2 == 0 and num // 2 > 1) or (num % 3 == 0 and num // 3 > 1):
    #             continue
    #         if num in primeList:
    #             primeCount += 1
    #             continue
    #         divideCheck = True
    #         if num == 1:
    #             divideCheck = False
    #         for primeCheck in range(2, round(num ** (1 / 2)) + 1):
    #             if num % primeCheck == 0:
    #                 divideCheck = False
    #                 break
    #         if divideCheck == True:
    #             primeList.append(num)
    #             primeCount += 1
    #     sys.stdout.write(str(primeCount) + '\n')
    # return
