import sys


def solution():
    stairNum = int(sys.stdin.readline().strip())
    scoreList = []
    for _ in range(stairNum):
        scoreList.append(int(sys.stdin.readline().strip()))

    answerList = [0] * (stairNum + 1)

    for i in range(stairNum + 1):
        if i == 0:
            continue
        elif i == 1:
            answerList[i] = scoreList[i - 1]
        elif i == 2:
            answerList[i] = scoreList[i - 1] + scoreList[i - 2]
        else:
            answerList[i] = max(scoreList[i - 1] + scoreList[i - 2] + answerList[i - 3], scoreList[i - 1] + answerList[i - 2])

    sys.stdout.write(str(answerList[-1]) + '\n')

    return


if __name__ == '__main__':
    solution()
