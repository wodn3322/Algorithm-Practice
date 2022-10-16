def solution(n):
    answer = 0

    while True:
        if n ==1:
            answer+=1
            break
        else:
            if n%2 ==0:
                n//=2
            else:
                n-=1
                answer+=1
    print(answer)
    return answer


if __name__ == '__main__':
    num = 6
    solution(num)
