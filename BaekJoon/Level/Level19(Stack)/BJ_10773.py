import sys

def solution():
    numCount = int(sys.stdin.readline().strip())
    callList = [0]*numCount
    answerList = []
    for i in range(numCount):
        callList[i] = int(sys.stdin.readline().strip())

    for c in callList:
        if c == 0:
            answerList.pop()
        else:
            answerList.append(c)

    sys.stdout.write(str(sum(answerList))+'\n')

    return


if __name__ == '__main__':
    solution()
