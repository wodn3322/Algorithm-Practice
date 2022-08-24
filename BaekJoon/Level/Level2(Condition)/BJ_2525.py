def solution():
    a, b = input().split(" ")
    a, b = int(a), int(b)
    c = int(input())
    if b + c >= 60:
        hour = (b + c) // 60
        if a + hour >= 24:
            print(str(a + hour - 24) + " " + str((b + c) % 60))
        else:
            print(str(a + hour) + " " + str((b + c) % 60))
    else:
        print(str(a) + " " + str(b + c))
    return


if __name__ == '__main__':
    solution()
