# !!!!!!! 특이점 !!!!!!!!!

# 1. 메모리 사용량으로 리스트를 줄임
def solution():
    num = int(input())
    if num == 1:
        return
    primeList = []
    roundNum = round(num ** (1 / 2))
    for i in range(2, roundNum + 1):
        for prime in range(2, i + 1):
            if i == prime and i <= roundNum:
                primeList.append(i)

            if i % prime == 0:
                break
    if len(primeList) == 0:
        primeList.append(num)
    # numPrimeDivideList = []
    for i in primeList:
        while num % i == 0:
            # numPrimeDivideList.append(i)
            print(i)
            num = num // i
    if num != 1:
        print(num)
        # numPrimeDivideList.append(num)
    # for i in numPrimeDivideList:
    #     print(i)


# 2. system 함수를 이용
# print, input 함수보다 sys.stdout.write, sys.stdin.readline 함수가 더 메모리 사용량이 적음

import sys


def solution2():
    num = int(input())
    if num == 1:
        return
    primeList = []
    roundNum = round(num ** (1 / 2))
    for i in range(2, roundNum + 1):
        for prime in range(2, i + 1):
            if i == prime and i <= roundNum:
                primeList.append(i)

            if i % prime == 0:
                break
    if len(primeList) == 0:
        primeList.append(num)
    numPrimeDivideList = []
    for i in primeList:
        while num % i == 0:
            numPrimeDivideList.append(i)
            # print(i)
            num = num // i
    if num != 1:
        # print(num)
        numPrimeDivideList.append(num)
    for i in numPrimeDivideList:
        sys.stdout.write(str(i) + "\n")

    return


if __name__ == '__main__':
    solution()
    # solution2()
