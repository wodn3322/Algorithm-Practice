import sys


def solution():
    n, k = map(int, sys.stdin.readline().strip().split(' '))
    lanList = []
    for _ in range(n):
        lanList.append(int(sys.stdin.readline().strip()))

    start = 1
    end = max(lanList)

    while start <= end:
        count = 0
        print(start, end)
        mid = (start + end) // 2
        for l in lanList:
            count += l // mid
        if count >= k:
            start = mid + 1
        else:
            end = mid - 1
    print(end)

    return


if __name__ == '__main__':
    solution()
