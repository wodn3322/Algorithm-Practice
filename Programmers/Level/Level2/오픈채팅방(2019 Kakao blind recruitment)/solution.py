def solution(record):
    answer = []
    dataDict = dict()
    printList = []
    for r in record:
        dataList = r.split(' ')
        if dataList[0] == 'Change':
            dataDict[dataList[1]] = dataList[2]
        elif dataList[0] == 'Enter':
            dataDict[dataList[1]] = dataList[2]
            printList.append([dataList[1], '님이 들어왔습니다.'])
        elif dataList[0] == 'Leave':
            printList.append([dataList[1], '님이 나갔습니다.'])

    for p in printList:
        answer.append(dataDict[p[0]] + p[1])

    return answer


if __name__ == '__main__':
    recordList = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    solution(recordList)
