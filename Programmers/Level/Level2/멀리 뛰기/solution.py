def solution(n):
    answer = 0
    oneCount = n
    twoCount = 0
    while oneCount >= 0:
        topNum = 1
        botNum = 1
        totalCount = oneCount + twoCount
        for i in range(totalCount):
            topNum *= (i + 1)
            if i < oneCount:
                botNum *= (oneCount - i)
            if i < twoCount:
                botNum *= (twoCount - i)
        answer += topNum // botNum
        oneCount -= 2
        twoCount += 1
    answer %= 1234567
    return answer


if __name__ == '__main__':
    num = 4
    solution(num)
