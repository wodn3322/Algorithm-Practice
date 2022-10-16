def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations) + 1):
        qutation = 0
        unqutation = 0
        for c in citations:
            if c >= i:
                qutation += 1

            if c <= i:
                unqutation += 1

        if qutation >= i and qutation >= unqutation:
            answer = i

    return answer


if __name__ == '__main__':
    citaList = [3, 0, 6, 1, 5]
    solution(citaList)
