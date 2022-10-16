import sys


def solution():
    e, s, m = map(int, sys.stdin.readline().strip().split())
    eLoop, sLoop, mLoop = 16, 29, 20
    i = 1
    eNum, sNum, mNum = 1, 1, 1
    while True:
        if eNum == e and sNum == s and mNum == m:
            break
        eNum += 1
        sNum += 1
        mNum += 1
        if eNum == eLoop:
            eNum -= 15
        if sNum == sLoop:
            sNum -= 28
        if mNum == mLoop:
            mNum -= 19
        i += 1

    sys.stdout.write(str(i) + '\n')
    return


if __name__ == '__main__':
    solution()
