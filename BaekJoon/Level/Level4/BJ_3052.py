def solution():
    remainList = []
    for _ in range(10):
        a = int(input())
        remaineder = a % 42
        if remaineder not in remainList:
            remainList.append(remaineder)

    print(len(remainList))

    return


if __name__ == '__main__':
    solution()
