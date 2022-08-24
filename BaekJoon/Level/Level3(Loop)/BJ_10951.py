def solution():
    while True:
        try:
            a, b = map(int, input().split(" "))
            print(a + b)
        except:
            break

    return


if __name__ == '__main__':
    solution()
