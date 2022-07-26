def solution():
    maxNum = 0
    maxNumLine = 0

    for i in range(9):
        inputNum = int(input())
        if maxNum < inputNum:
            maxNum = inputNum
            maxNumLine = (i + 1)

    print(maxNum)
    print(maxNumLine)

    return


if __name__ == '__main__':
    solution()
