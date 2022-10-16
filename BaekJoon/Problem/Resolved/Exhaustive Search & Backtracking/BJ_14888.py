import sys


def solution():
    size = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().strip().split(' ')))
    operList = list(map(int, sys.stdin.readline().strip().split(' ')))
    answerList = []
    nowNum = numList[0]

    def BruteForce(loc, oper, now):
        if sum(oper) == 0:
            answerList.append(now)
            return

        for i in range(4):
            if oper[i] != 0:
                oper[i] -= 1
                if i == 0:
                    BruteForce(loc + 1, oper, now + numList[loc])
                elif i == 1:
                    BruteForce(loc + 1, oper, now - numList[loc])
                elif i == 2:
                    BruteForce(loc + 1, oper, now * numList[loc])
                else:
                    if now < 0:
                        BruteForce(loc + 1, oper, -(abs(now) // numList[loc]))
                    else:
                        BruteForce(loc + 1, oper, now // numList[loc])
                oper[i] += 1

    BruteForce(1, operList, nowNum)
    sys.stdout.write(str(max(answerList)) + '\n')
    sys.stdout.write(str(min(answerList)) + '\n')
    return


if __name__ == '__main__':
    solution()
