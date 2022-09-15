def solution(brown, yellow):
    answer = []
    for i in range(1, brown//2):

        if i * (brown // 2) + i * 2 - i ** 2 == brown + yellow:
            if i > brown//2 + 2 - i:
                answer.append(i)
                answer.append(brown//2 + 2 - i)
            else:
                answer.append(brown//2 + 2 - i)
                answer.append(i)
            break
    return answer


if __name__ == '__main__':
    b = 10
    y = 2
    solution(b, y)

# h = brown // 2 + 2 - m
