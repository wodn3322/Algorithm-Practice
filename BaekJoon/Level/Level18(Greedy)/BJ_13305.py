import sys


def solution():
    cityNum = int(sys.stdin.readline().strip())
    cityDistanceList = list(map(int, sys.stdin.readline().strip().split(' ')))
    cityOilPrice = list(map(int, sys.stdin.readline().strip().split(' ')))
    cityOilPrice.pop()

    price = 0
    distance = 0
    oilPrice = 0
    for i in range(cityNum - 1):
        if i == 0:
            oilPrice = cityOilPrice[i]
            distance += cityDistanceList[i]
        else:
            if oilPrice > cityOilPrice[i]:
                price += (oilPrice * distance)
                oilPrice = cityOilPrice[i]
                distance = cityDistanceList[i]
            else:
                distance += cityDistanceList[i]
        if i == cityNum - 2:
            price += (oilPrice * distance)

    sys.stdout.write(str(price) + '\n')

    return


if __name__ == '__main__':
    solution()
