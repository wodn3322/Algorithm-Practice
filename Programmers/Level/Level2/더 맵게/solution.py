import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        firstNum = heapq.heappop(scoville)
        secondNum = heapq.heappop(scoville)
        heapq.heappush(scoville, firstNum + secondNum * 2)
        answer += 1

    if scoville[0] < K:
        answer = -1

    return answer


if __name__ == '__main__':
    # scoList, kNum = [1, 2, 3, 9, 10, 12], 7
    scoList, kNum = [1, 1, 1], 1000
    solution(scoList, kNum)
