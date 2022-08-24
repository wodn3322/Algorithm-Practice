import sys


def solution():
    inputList = []
    while True:
        inputString = sys.stdin.readline().strip()
        if inputString != '0 0 0':
            inputList.append(list(map(int, inputString.split(' '))))
        else:
            break

    for i in inputList:
        maxNum = max(i)
        i.remove(maxNum)
        if maxNum ** 2 == i[0] ** 2 + i[1] ** 2:
            sys.stdout.write('right\n')
        else:
            sys.stdout.write('wrong\n')

    return


if __name__ == '__main__':
    solution()
