import math

def solution(fees, records):
    answer = []

    recordDict = {}
    recordStack = []
    carList =[]
    for r in records:
        rList = r.split(' ')
        if rList[2] == 'IN':
            recordStack.append(rList[:2])
        else:
            for i in recordStack:
                if rList[1] == i[1]:
                    startTime = list(map(int, i[0].split(':')))
                    endTime = list(map(int, rList[0].split(':')))
                    time = (endTime[0] - startTime[0]) * 60 + endTime[1] - startTime[1]
                    if rList[1] in recordDict:
                        recordDict[rList[1]] += time
                    else:
                        recordDict[rList[1]] = time
                    if rList[1] not in carList:
                        carList.append(rList[1])
                    recordStack.remove(i)
                    break
    if len(recordStack) != 0:
        for r in recordStack:
            startTime = list(map(int, r[0].split(':')))
            if r[1] in recordDict:
                recordDict[str(r[1])] += ((23 - startTime[0]) * 60 + 59 - startTime[1])
            else:
                recordDict[str(r[1])] = ((23 - startTime[0]) * 60 + 59 - startTime[1])
                carList.append(r[1])

    carList.sort()
    for car in carList:
        time = recordDict[car]
        if time>fees[0]:
            bill = fees[1]+math.ceil((time-fees[0])/fees[2])*fees[3]
        else:
            bill = fees[1]
        answer.append(bill)

    return answer


if __name__ == '__main__':
    freeList = [1, 461, 1, 10]
    recordList = ["00:00 1234 IN"]
    solution(freeList, recordList)
