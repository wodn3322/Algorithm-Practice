def solution(n,a,b):
    answer = 0

    while True:
        if a %2 ==1  and a+1 ==b:
            answer+=1
            break
        else:
            a = a//2 +a %2
            b = b//2 +b%2
            answer+=1

    return answer


if __name__ == '__main__':
    N = 8
    A=4
    B=7
    solution(N,A,B)
