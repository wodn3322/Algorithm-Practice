def solution():
    a, b, v = map(int, input().split(" "))

    dayCount = (v - a) // (a - b)
    if (v - a) % (a - b) == 0:
        print(dayCount + 1)
    else:
        print(dayCount + 2)

    return


if __name__ == '__main__':
    solution()
