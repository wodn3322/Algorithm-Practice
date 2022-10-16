import sys


def solution():
    answerList = []

    while True:
        inputString = input().strip()
        if inputString == '0':
            break

        frontString = inputString[:(len(inputString) // 2 + len(inputString) % 2)]
        backString = inputString[len(inputString) // 2:]
        backString = backString[::-1]

        if frontString == backString:
            answerList.append('yes')
        else:
            answerList.append('no')
    for a in answerList:
        print(a)

    return


if __name__ == '__main__':
    solution()
