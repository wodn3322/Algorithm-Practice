def solution():
    a, b = map(int, input().split(" "))

    for i in range(a, b + 1):
        checkDivide = True
        if i == 1:
            continue
        if (i % 2 == 0 and i // 2 > 1) or (i % 3 == 0 and i // 3 > 1):
            continue
        for j in range(2, round(i ** (1 / 2)) + 1):
            if i % j == 0:
                checkDivide = False
                break
        if checkDivide:
            print(i)
    return


if __name__ == '__main__':
    solution()
