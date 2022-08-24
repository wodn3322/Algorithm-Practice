def solution():
    num = int(input())
    count = 0
    changeNum = num
    while True:
        a = changeNum // 10
        b = changeNum % 10
        c = (a + b) % 10
        changeNum = int(str(b) + str(c))
        count += 1
        if num == changeNum:
            print(count)
            break
    return


if __name__ == '__main__':
    solution()
