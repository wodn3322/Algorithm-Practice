def solution():
    inputString = input().lower()
    checkDict = {}
    inputStringList = list(inputString)

    for i in list(set(inputStringList)):
        checkDict[i] = inputString.count(i)

    maxNum = 0
    maxChar = ""
    overlap = 0

    for i in checkDict:
        if checkDict[i] > maxNum:
            maxNum = checkDict[i]
            maxChar = i
            overlap = 1
        elif checkDict[i] == maxNum:
            overlap += 1

    if overlap == 1:
        print(maxChar.upper())
    else:
        print("?")

    return


if __name__ == '__main__':
    solution()
