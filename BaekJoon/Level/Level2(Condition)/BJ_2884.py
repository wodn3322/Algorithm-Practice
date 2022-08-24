def solution():
    a, b = input().split(" ")
    a, b = int(a), int(b)
    if b < 45:
        restMin = 45 - b
        if a > 0:
            print(str(a - 1) + " " + str(60 - restMin))
        else:
            print("23 " + str(60 - restMin))
    else:
        print(str(a) + " " +str(b - 45))
    return


if __name__ == '__main__':
    solution()
