import sys


def solution():
    n, m = map(int,sys.stdin.readline().strip().split(' '))

    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    answer =0
    # 상하
    answer += 2*(m*n)
    # 앞뒤 1
    num = 0
    for g in graph:
        num+=max(g)
    answer+=2*num
    # 앞뒤 2
    



    return


if __name__ == '__main__':
    solution()
