import sys


def solution():
    num = int(sys.stdin.readline().strip())
    graph = []
    team1 = []
    answerList = []
    for _ in range(num):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    def checkScore():
        score1 = 0
        score2 = 0
        team2 = []
        for i in range(num):
            if i not in team1:
                team2.append(i)

        for i in range(num // 2):
            for j in range(i + 1, num // 2):
                score1 += (graph[team1[i]][team1[j]] + graph[team1[j]][team1[i]])
                score2 += (graph[team2[i]][team2[j]] + graph[team2[j]][team2[i]])
        answerList.append(abs(score1 - score2))

    def makeTeam(n):
        if len(team1) == num // 2:
            checkScore()
            return
        else:
            for i in range(n, num):
                team1.append(i)
                makeTeam(i + 1)
                team1.pop()

    makeTeam(0)
    sys.stdout.write(str(min(answerList)) + '\n')

    return


if __name__ == '__main__':
    solution()
