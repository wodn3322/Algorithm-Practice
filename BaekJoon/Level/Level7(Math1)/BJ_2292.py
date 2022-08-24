def solution():
    roomNum = int(input())
    passRoomCount = 0
    loopCount = 0
    roomNum -= 1

    while True:
        roomNum -= loopCount * 6
        passRoomCount += 1
        if roomNum <= 0:
            print(passRoomCount)
            return
        loopCount += 1


if __name__ == '__main__':
    solution()
