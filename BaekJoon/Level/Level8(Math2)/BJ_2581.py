def solution():
    minNum =  int(input())
    maxNum = int(input())
    primeList = []
    for num in range(minNum, maxNum + 1):
        if num == 2:
            primeList.append(num)
            continue
        for i in range(2, num):
            if num % i == 0:
                break
            if i == num - 1:
                primeList.append(num)
    if len(primeList) != 0:
        print(sum(primeList))
        print(min(primeList))
    else:
        print(-1)
    return


if __name__ == '__main__':
    solution()
