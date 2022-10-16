def solution(n, k):
    answer = -1
    numString = ''

    while n // k > 0:
        temp = n % k
        numString = str(temp) + numString
        n //= k
    numString = str(n) + numString
    transList = numString.split('0')
    answerList = []

    for i in transList:
        if len(i)==0 or int(i)<2:
            continue
        else:
            checkDivide = True
            for j in range(2,round(int(i)**(1/2))+1):
                if int(i)%j==0:
                    checkDivide=False
                    break
            if checkDivide:
                answerList.append(i)
    answer = len(answerList)
    print(answer)
    return answer


if __name__ == '__main__':
    num = 437674
    divideType = 3
    solution(num, divideType)
