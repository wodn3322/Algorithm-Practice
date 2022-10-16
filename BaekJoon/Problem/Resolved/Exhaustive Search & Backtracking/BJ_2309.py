import sys


def solution():
    dwarfList = []

    for _ in range(9):
        dwarfList.append(int(sys.stdin.readline().strip()))
    dwarfList.sort()
    for i in range(8):
        for j in range(i + 1, 9):
            d1 = dwarfList[i]
            d2 = dwarfList[j]
            listSum = sum(dwarfList)

            if listSum - (d1 + d2) == 100:
                dwarfList.remove(d1)
                dwarfList.remove(d2)
                break
        if len(dwarfList) == 7:
            break

    for d in dwarfList:
        sys.stdout.write(str(d) + '\n')

    return


if __name__ == '__main__':
    solution()
