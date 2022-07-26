def solution():
    inputLenght = int(input())
    scoreList = []
    for _ in range(inputLenght):
        inputString = input()
        inputStringList = list(filter(None, inputString.split("X")))
        sum = 0
        for i in inputStringList:
            for i in range(1, 1 + len(i)):
                sum += i
        scoreList.append(sum)
    for i in scoreList:
        print(i)
    return


if __name__ == '__main__':
    solution()
