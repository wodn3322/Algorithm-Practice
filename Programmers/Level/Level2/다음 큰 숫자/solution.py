def solution(n):
    answer = 0
    oneCount = str(bin(n)).count('1')
    for i in range(n+1,1000001):
        if str(bin(i)).count('1')==oneCount:
            answer = i
            break
    return answer


if __name__ == '__main__':
    num = 78
    solution(num)
