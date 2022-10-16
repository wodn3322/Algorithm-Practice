from collections import deque

count = 0


def solution(m, n, board):
    global count
    answer = 0
    graph = []
    checked = [[0] * n for _ in range(m)]
    deleteList = set

    for b in board:
        graph.append(list(b))
        print(b)

    def checkBox(x, y):
        if graph[x][y] == graph[x + 1][y] == graph[x][y + 1] == graph[x + 1][y + 1] != '':
            deleteList.add((x, y))
            deleteList.add([x + 1, y])
            deleteList.add([x, y + 1])
            deleteList.add([x + 1, y + 1])

    while True:

        for i in range(m - 1):
            for j in range(n - 1):
                checkBox(i, j)

    print(answer)
    return answer


if __name__ == '__main__':
    # solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
    # solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
    solution(8, 5, ['HGNHU', 'CRSHV', 'UKHVL', 'MJHQB', 'GSHOT', 'MQMJJ', 'AGJKK', 'QULKK'])
