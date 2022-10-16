def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)

    print(answer)

    return answer


if __name__ == '__main__':
    num = 4
    lnum = 7
    rnum = 14
    solution(num, lnum, rnum)
