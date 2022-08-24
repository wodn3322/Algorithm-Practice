def solution():
    inputCount = int(input())
    inputList = []
    primeList = []

    for _ in range(inputCount):
        inputList.append(int(input()))

    for i in range(2, 10000):
        checkDivide = True
        for prime in range(2, round(i ** (1 / 2)) + 1):
            if i % prime == 0:
                checkDivide = False
                break
        if checkDivide:
            primeList.append(i)

    for i in inputList:
        a = i / 2
        b = i / 2
        while True:
            if a in primeList and b in primeList:
                print(str(int(a)) + " " + str(int(b)))
                break
            else:
                a -= 1
                b += 1

    return


if __name__ == '__main__':
    solution()
