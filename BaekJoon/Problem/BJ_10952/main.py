def solution():
    arrA = []
    arrB = []
    while (1):
        a,b = input().split(" ")
        a=int(a)
        b=int(b)
        # b = int(input())
        if a == 0 and b == 0:
            break
        else:
            arrA.append(a)
            arrB.append(b)

    for i in range(arrA):
        print(arrA[i] + arrB[i])


if __name__ == '__main__':
    solution()
