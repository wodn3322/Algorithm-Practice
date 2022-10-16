import sys


def solution():
    n, l = map(int, sys.stdin.readline().strip().split(' '))

    graph = []
    answer = 0

    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    # 가로
    def checkRow(r):
        runway = [0] * n
        for c in range(n - 1):
            if abs(graph[r][c] - graph[r][c + 1]) > 1:
                return False
            elif graph[r][c] - graph[r][c + 1] == 0:
                continue
            elif graph[r][c] < graph[r][c + 1]:
                for j in range(c - l + 1, c + 1):
                    if j < 0 or graph[r][c] != graph[r][j] or runway[j] != 0:
                        return False
                    else:
                        runway[j] = 1
            elif graph[r][c] > graph[r][c + 1]:
                for j in range(c + 1, c + l + 1):
                    if j >= n or graph[r][c + 1] != graph[r][j] or runway[j] != 0:
                        return False
                    else:
                        runway[j] = 1
        return True

    def checkCol(c):
        runway = [0] * n
        for r in range(n - 1):
            if abs(graph[r][c] - graph[r + 1][c]) > 1:
                return False
            elif graph[r][c] == graph[r + 1][c]:
                continue
            elif graph[r][c] < graph[r + 1][c]:
                for j in range(r - l + 1, r + 1):
                    if j < 0 or graph[r][c] != graph[j][c] or runway[j] != 0:
                        return False
                    else:
                        runway[j] = 1
            elif graph[r][c] > graph[r + 1][c]:
                for j in range(r + 1, r + l + 1):
                    if j >= n or graph[r + 1][c] != graph[j][c] or runway[j] != 0:
                        return False
                    else:
                        runway[j] = 1
        return True

    for i in range(n):
        if checkRow(i):
            answer += 1
        if checkCol(i):
            answer += 1

    sys.stdout.write(str(answer) + '\n')

    return


if __name__ == '__main__':
    solution()
