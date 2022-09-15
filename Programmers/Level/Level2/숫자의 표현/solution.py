def solution(n):
    answer = 0
    i=0
    loopCount =0
    while True:
        i+=1
        loopCount+=i
        if n< loopCount:
            break
        else:
            if (n-loopCount)%i==0:
                answer+=1

    print(answer)

    return answer


if __name__ == '__main__':
    num = 15
    solution(num)
