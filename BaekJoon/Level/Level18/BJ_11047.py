import sys


def solution():
    coinNum, price = map(int, sys.stdin.readline().strip().split())
    coinList = [0] * coinNum

    for i in range(coinNum):
        coinList[i] = int(sys.stdin.readline().strip())

    coinList = sorted(coinList, reverse=True)
    minCoinCount = 0
    for coin in coinList:
        if price >= coin:
            minCoinCount += (price // coin)
            price = price % coin

        if price ==0:
            break

    sys.stdout.write(str(minCoinCount)+'\n')

    return


if __name__ == '__main__':
    solution()
