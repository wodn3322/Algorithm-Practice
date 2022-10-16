import sys


def solution():
    n, m = map(int, sys.stdin.readline().strip().split(' '))

    boardList = []

    for _ in range(n):
        boardList.append(list(sys.stdin.readline().strip()))

    minCount = n * m
    for i in range(n - 7):
        for j in range(m - 7):
            cnt1 = 0
            cnt2 = 0
            for a in range(8):
                for b in range(8):
                    if (a + b) % 2 == 1:
                        if boardList[i + a][j + b] == 'B':
                            cnt1 += 1
                        if boardList[i + a][j + b] == 'W':
                            cnt2 += 1
                    else:
                        if boardList[i + a][j + b] == 'W':
                            cnt1 += 1
                        if boardList[i + a][j + b] == 'B':
                            cnt2 += 1

            minCount = min(minCount, cnt1, cnt2)
    sys.stdout.write(str(minCount) + '\n')

    return


if __name__ == '__main__':
    solution()
