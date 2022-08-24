def solution():
    num = int(input())
    count = 1
    startNum = 666
    while True:
        if count == num:
            break
        startNum += 1
        if '666' in str(startNum):
            count += 1

    print(startNum)

    return


if __name__ == '__main__':
    solution()
