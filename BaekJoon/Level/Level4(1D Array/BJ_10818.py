def solution():
    length = int(input())
    inputList = list(map(int, input().split(" ")))
    if len(inputList) != length:
        return
    print(min(inputList), max(inputList))

    return


if __name__ == '__main__':
    solution()
