import sys

def solution():
    numLength, divideNum = map(int, sys.stdin.readline().strip().split(' '))
    numList = list(map(int, sys.stdin.readline().strip().split(' ')))

    cumlativeList = [0] * (numLength)
    cumDivideList = [0] * divideNum

    # 누적합 리스트 생성 시 나머지 리스트를 만들어 바로 갯수 파악 -> 시간 초과 해결
    for i in range(numLength):
        if i == 0:
            cumlativeList[i] = numList[i] % divideNum
            cumDivideList[cumlativeList[i]] += 1
        else:
            cumlativeList[i] = (cumlativeList[i - 1] + numList[i]) % divideNum
            cumDivideList[cumlativeList[i]] += 1

    total = 0
    for i in range(len(cumDivideList)):
        if i == 0:
            total += cumDivideList[i]
        total += (cumDivideList[i] * (cumDivideList[i] - 1)) // 2

    sys.stdout.write(str(total) + '\n')

    # 나머지의 갯수를 count함수를 통해 찾아 조합 -> 시간 초
    # for i in range(divideNum):
    #     partCount = 0
    #     partNum = cumlativeList.count(i)
    #     if i == 0:
    #         partCount += partNum
    #     partCount += (partNum * (partNum - 1)) // 2
    #     total += partCount

    # 하나하나 범위를 찾은 경우과 -> 시간 초과
    # count =0
    # for i in range(numLength):
    #     sum =0
    #     for j in range(i,numLength):
    #         sum +=numList[j]
    #         if sum % 3 ==0:
    #             count+=1
    # print(count)

    return


if __name__ == '__main__':
    solution()
