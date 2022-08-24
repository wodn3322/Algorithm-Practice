import sys


def solution():
    personCount = int(sys.stdin.readline().strip())
    personList = [[]] * personCount

    for i in range(personCount):
        personList[i] = sys.stdin.readline().split()
        personList[i][0] = int(personList[i][0])

    personList.sort(key=lambda x: x[0])
    for person in personList:
        sys.stdout.write(str(person[0]) + ' ' + person[1] + '\n')

    return


if __name__ == '__main__':
    solution()
