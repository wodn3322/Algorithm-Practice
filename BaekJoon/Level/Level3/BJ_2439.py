def solution():
    loop = int(input())
    for i in range(loop):
        star = ""
        for j in range(1, loop - i):
            star += " "
        for j in range(i + 1):
            star += "*"
        print(star)
    return


if __name__ == '__main__':
    solution()
