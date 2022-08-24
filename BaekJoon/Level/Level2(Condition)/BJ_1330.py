def solution():
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")
    return


if __name__ == '__main__':
    solution()
