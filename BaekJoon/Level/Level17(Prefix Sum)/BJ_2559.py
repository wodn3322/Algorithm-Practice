import sys


def solution():
    dayLength, continuday = map(int, sys.stdin.readline().strip().split(' '))
    dayTemperatureList = list(map(int, sys.stdin.readline().strip().split(' ')))
    cumulativeList = [0] * (dayLength - continuday + 1)

    daySum = 0

    for i in range(continuday):
        daySum += dayTemperatureList[i]
    cumulativeList[0] = daySum

    for i in range(1, len(cumulativeList)):
        cumulativeList[i] = cumulativeList[i - 1] - dayTemperatureList[i - 1] + dayTemperatureList[i - 1 + continuday]

    sys.stdout.write(str(max(cumulativeList)) + '\n')

    return


if __name__ == '__main__':
    solution()
