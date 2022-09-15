def solution(n):
    answer = 0
    fifoList = [0, 1]
    for i in range(n + 1):
        if i > 1:
            fifoList.append(fifoList[i - 1] + fifoList[i - 2])

    answer = fifoList[-1] % 1234567
    return answer


if __name__ == '__main__':
    num = 1500
    solution(num)
