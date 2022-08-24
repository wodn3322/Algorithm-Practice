def solution():
    deliveryAmount = int(input())

    threeCount = deliveryAmount // 3
    fiveCount = 0
    if deliveryAmount % 3 == 0:
        if threeCount >= 5:
            while threeCount >= 5:
                fiveCount += 3
                threeCount -= 5
            print(fiveCount + threeCount)
            return
        else:
            print(fiveCount + threeCount)
            return
    elif deliveryAmount % 3 == 1:
        if threeCount >= 3:
            fiveCount += 2
            threeCount -= 3
            while threeCount >= 5:
                fiveCount += 3
                threeCount -= 5
            print(fiveCount + threeCount)
            return

    elif deliveryAmount % 3 == 2:
        fiveCount += 1
        threeCount -= 1
        while threeCount >= 5:
            fiveCount += 3
            threeCount -= 5
        print(fiveCount + threeCount)
        return
    print(-1)

    return


if __name__ == '__main__':
    solution()
