import sys


def solution():
    n, m, x, y, k = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    dice = [0, 0, 0, 0, 0, 0]
    answer = []

    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    commandList = list(map(int, sys.stdin.readline().strip().split(' ')))

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def changeDice(dir):
        if dir == 1:
            newdDice = [dice[0], dice[5], dice[1], dice[2], dice[4], dice[3]]
        elif dir == 2:
            newdDice = [dice[0], dice[2], dice[3], dice[5], dice[4], dice[1]]
        elif dir == 3:
            newdDice = [dice[2], dice[1], dice[4], dice[3], dice[5], dice[0]]
        elif dir == 4:
            newdDice = [dice[5], dice[1], dice[0], dice[3], dice[2], dice[4]]
        return newdDice

    for command in commandList:
        nx = x + dx[command - 1]
        ny = y + dy[command - 1]
        if 0 <= nx < n and 0 <= ny < m:
            dice = changeDice(command)
            x, y = nx, ny
            if graph[x][y] != 0:
                dice[5] = graph[x][y]
                graph[x][y] = 0
                answer.append(dice[2])
            else:
                graph[x][y] = dice[5]
                answer.append(dice[2])
    for a in answer:
        sys.stdout.write(str(a) + '\n')
    return


if __name__ == '__main__':
    solution()
