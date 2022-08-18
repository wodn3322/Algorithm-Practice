import sys


def solution():
    stringA = list(sys.stdin.readline().strip())
    stringB = list(sys.stdin.readline().strip())

    dynamicList = [[0] * (len(stringA) + 1) for _ in range(len(stringB) + 1)]

    for i in range(len(stringB)):
        for j in range(len(stringA)):
            if stringB[i] == stringA[j]:
                dynamicList[i + 1][j + 1] = dynamicList[i][j] + 1
            else:
                dynamicList[i + 1][j + 1] = max(dynamicList[i][j + 1], dynamicList[i + 1][j])

    sys.stdout.write(str(dynamicList[-1][-1]) + '\n')
    return


if __name__ == '__main__':
    solution()
