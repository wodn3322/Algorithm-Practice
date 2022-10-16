def solution(prices):
    answer = []
    answer = [0] * len(prices)
    stackList = []

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            stackList.append(prices[j])
            if prices[i] > prices[j]:
                break
        answer[i] = len(stackList)
        stackList = []

    return answer


if __name__ == '__main__':
    priceList = [1, 2, 3, 2, 3]
    solution(priceList)
