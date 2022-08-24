import sys


def solution():
    width, height, x, y, p = map(int, sys.stdin.readline().strip('\n').split(' '))
    r = height/2
    personList = [[]]*p
    personNum = 0
    for i in range(p):
        personList[i] = (list(map(int,sys.stdin.readline().strip().split(' '))))
    for person in personList:

        leftDistance = ((person[0] - x) ** 2 + (person[1] - y - r) ** 2) ** (1 / 2)
        rightDistance = ((person[0] - x - width) ** 2 + (person[1] - y - r) ** 2) ** (1 / 2)
        if ((x <= person[0] <= (x + width)) and (y <= person[1] <= (y + 2 * r))) or leftDistance <= r or rightDistance <= r:
            personNum += 1
        else:
            continue

    sys.stdout.write(str(personNum) + '\n')

    return


if __name__ == '__main__':
    solution()
