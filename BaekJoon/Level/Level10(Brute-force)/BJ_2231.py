def solution():
    num = int(input())
    answer = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            if num == 100001 * a + 10001 * b + 1001 * c + 101 * d + 11 * e + 2 * f:
                                if answer==0:
                                    answer = 100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f
                                if answer> 100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f:
                                    answer= 100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f
    if answer == 0:
        print(0)
    else:
        print(answer)

    return


if __name__ == '__main__':
    solution()
