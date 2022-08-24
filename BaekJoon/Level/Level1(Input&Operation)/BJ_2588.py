def solution():
    a = int(input())
    b = int(input())
    print(a* (b%10))
    print(a*(b%100//10))
    print(a*(b//100))
    print(a*b)
    return


if __name__ == '__main__':
    solution()
