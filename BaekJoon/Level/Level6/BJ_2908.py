def solution():
    a, b = input().split(" ")
    a = int(a[::-1])
    b = int(b[::-1])
    if a > b:
        print(a)
    else:
        print(b)
    return


if __name__ == '__main__':
    solution()
