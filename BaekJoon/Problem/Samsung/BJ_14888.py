import sys


def solution():
    numCount = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().strip().split(' ')))
    operList = list(map(int, sys.stdin.readline().strip().split(' ')))
    answerList = []

    def DFS(index, num):
        if sum(operList) == 0:
            answerList.append(num)
            return

        for i in range(4):
            if operList[i] != 0:
                operList[i] -= 1
                if i == 0:
                    DFS(index + 1, num + numList[index])
                elif i == 1:
                    DFS(index + 1, num - numList[index])
                elif i == 2:
                    DFS(index + 1, num * numList[index])
                elif i == 3:
                    if num < 0:
                        DFS(index + 1, -(abs(num) // numList[index]))
                    else:
                        DFS(index + 1, num // numList[index])
                operList[i] += 1

    DFS(1, numList[0])
    print(max(answerList))
    print(min(answerList))

    return


if __name__ == '__main__':
    solution()
