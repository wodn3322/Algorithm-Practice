def solution():
    count = int(input())
    numList = []
    for _ in range(count):
        numList.append(int(input()))

    numList.sort()

    for i in numList:
        print(i)

    return


if __name__ == '__main__':
    solution()
