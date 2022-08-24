def solution():
    a = int(input())
    b = int(input())
    c = int(input())
    mul = a * b * c
    for i in range(10):
        print(str(mul).count(str(i)))
    print(ord("A"))
    return



if __name__ == '__main__':
    solution()
