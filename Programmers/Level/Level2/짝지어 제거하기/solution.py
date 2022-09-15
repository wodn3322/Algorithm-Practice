def solution(s):
    answer = -1
    stringList = list(s)

    stackList = []
    for i in stringList:
        if len(stackList) == 0:
            stackList.append(i)
            continue
        if i != stackList[-1]:
            stackList.append(i)
        else:
            stackList.pop()
    if len(stackList) != 0:
        answer = 0
    else:
        answer = 1

    return answer


if __name__ == '__main__':
    inputString = 'baabaa'
    solution(inputString)
