def solution():
    a, b, c, = map(int, input().split(" "))
    diff = c - b
    if diff <= 0:
        print(-1)
        return

    print(a // diff + 1)

    return


if __name__ == '__main__':
    solution()
