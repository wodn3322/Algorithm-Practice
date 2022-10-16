import sys

input = sys.stdin.readline


def solution():
    answerList = []

    n = int(input())
    nList = set(list(map(int, input().split(' '))))
    m = int(input())
    mList = list(map(int, input().split(' ')))

    for num in mList:
        if num in nList:
            answerList.append(1)
        else:
            answerList.append(0)

    for a in answerList:
        print(a)

    return


if __name__ == '__main__':
    solution()
