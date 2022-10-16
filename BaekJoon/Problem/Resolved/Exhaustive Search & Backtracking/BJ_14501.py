import sys

answer = 0


def solution():
    global answer
    remain = int(sys.stdin.readline().strip())
    consultList = []
    answerList = [0] * (remain + 1)

    for _ in range(remain):
        consultList.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    # Brute force
    def BruteForce(day, pay):
        global answer
        if day == remain:
            answer = max(answer, pay)
            return
        if day > remain:
            return
        BruteForce(day + consultList[day][0], pay + consultList[day][1])
        BruteForce(day+1, pay)

    BruteForce(0, 0)

    sys.stdout.write(str(answer) + '\n')

    # DP
    for i in range(remain - 1, -1, -1):
        if i + consultList[i][0] > remain:
            answerList[i] = answerList[i + 1]
        else:
            answerList[i] = max(answerList[i + 1], consultList[i][1] + answerList[i + consultList[i][0]])
    print(answerList[0])
    return


if __name__ == '__main__':
    solution()
