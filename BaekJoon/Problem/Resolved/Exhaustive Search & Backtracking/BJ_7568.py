import sys


def solution():
    personNum = int(sys.stdin.readline().strip())
    personList = []
    answerList = [1] * personNum
    for _ in range(personNum):
        personList.append(list(map(int, sys.stdin.readline().strip().split())))

    for i in range(personNum):
        person1 = personList[i]
        for j in range(i + 1, personNum):
            person2 = personList[j]
            if person1[0] > person2[0] and person1[1] > person2[1]:
                answerList[j] += 1
            elif person1[0] < person2[0] and person1[1] < person2[1]:
                answerList[i] += 1

    for a in answerList:
        sys.stdout.write(str(a)+' ')
    sys.stdout.write('\n')

    return


if __name__ == '__main__':
    solution()
