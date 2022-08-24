def solution():
    length = int(input())
    inputString = input()
    sum = 0
    for i in range(length):
        sum += int(inputString[i])
    print(sum)
    return


if __name__ == '__main__':
    solution()
