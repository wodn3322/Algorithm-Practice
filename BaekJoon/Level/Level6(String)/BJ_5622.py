def solution():
    dial = {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}
    inputStringList = list(input())
    totalTime = 0
    for i in inputStringList:
        for d in dial:
            if i in d:
                totalTime += (dial[d] + 1)
    print(totalTime)
    return


if __name__ == '__main__':
    solution()
