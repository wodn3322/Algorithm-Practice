from collections import deque

def solution(priorities, location):
    answer = 0

    dequePrior = deque(priorities)
    topPriority = max(dequePrior)
    while True:
        if dequePrior[0] ==topPriority :
            if location == 0:
                answer+=1
                break
            else:
                dequePrior.popleft()
                topPriority=max(dequePrior)
                answer+=1
                location-=1
        else:
            if location ==0:
                location = len(dequePrior)-1
            else:
                location-=1
            dequePrior.rotate(-1)
    return answer


if __name__ == '__main__':
    priorityList = [1, 1, 9, 1, 1, 1]
    locationNum = 0
    solution(priorityList, locationNum)
