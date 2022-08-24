def solution():
    a, b, c = map(int, input().split(" "))

    if a == b and b == c:
        print(10000 + a * 1000)
    elif a == b and b != c:
        print(1000 + 100 * a)
    elif a == c and c != b:
        print(1000 + 100 * c)
    elif b == c and b != a:
        print(1000 + 100 * b)
    else:
        print(max(a, b, c) * 100)
    return


if __name__ == '__main__':
    solution()
