def solution():
    inputList = []
    while True:
        a,b = map(int, input().split(" "))
        if a != 0 and b != 0:
            inputList.append([a,b])
        else:
            break

    for i in inputList:
        print(i[0]+i[1])

    return


if __name__ == '__main__':
    solution()
