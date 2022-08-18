import sys


def solution():
    expression = list(sys.stdin.readline().strip())
    numList = []
    operationList = []
    num = ''
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-':
            operationList.append(expression[i])
            numList.append(int(num))
            num = ''
        else:
            num += expression[i]

        if i == len(expression) - 1:
            numList.append(int(num))

    minNum = numList[0]
    minusCheck = 0
    for i in range(len(operationList)):
        if minusCheck == 0:
            if operationList[i] == '+':
                minNum += numList[i + 1]
            else:
                minusCheck = 1
                minNum -= numList[i + 1]
        else:
            minNum -= numList[i + 1]
    print(minNum)

    return


if __name__ == '__main__':
    solution()
