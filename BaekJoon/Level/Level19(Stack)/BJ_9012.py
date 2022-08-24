import sys


def solution():
    caseNum = int(sys.stdin.readline().strip())
    caseList = []
    answerList = []
    for _ in range(caseNum):
        caseList.append(list(sys.stdin.readline().strip()))

    for case in caseList:
        leftPS = 0
        for i in range(len(case)):
            if i == 0 and case[i] == ')':
                answerList.append('NO')
                break
            else:
                if case[i] == '(':
                    leftPS += 1
                else:
                    leftPS -= 1
                    if leftPS < 0:
                        answerList.append('NO')
                        break

            if i == (len(case) - 1):
                if leftPS == 0:
                    answerList.append('YES')
                else:
                    answerList.append('NO')

    for answer in answerList:
        sys.stdout.write(answer + '\n')

    return


if __name__ == '__main__':
    solution()
