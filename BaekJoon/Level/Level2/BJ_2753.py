def solution():
    a = int(input())

    if a % 4 != 0:
        print("0")
        return
    else:
        if a % 100 != 0:
            print("1")
            return
        else:
            if a % 400 == 0:
                print("1")
            else:
                print("0")
    return


if __name__ == '__main__':
    solution()
