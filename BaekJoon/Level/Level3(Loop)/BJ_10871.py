def solution():
    length, standard = map(int, input().split(" "))
    inputList = list(input().split(" "))
    printList = []
    for i in inputList:
        if int(i) < standard:
            printList.append(i)

    for i in printList:
        print(i, end=" ")

    return


if __name__ == '__main__':
    solution()
