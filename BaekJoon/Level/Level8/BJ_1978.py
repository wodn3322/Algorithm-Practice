def solution():
    numCount = int(input())
    numList = list(map(int, input().split(" ")))
    primeList = []
    for num in numList:
        if num == 1:
            continue
        if num == 2:
            primeList.append(num)
            continue
        for i in range(2, num):
            if num % i == 0:
                break
            if i == num - 1:
                primeList.append(num)
    print(len(primeList))

    return


if __name__ == '__main__':
    solution()
