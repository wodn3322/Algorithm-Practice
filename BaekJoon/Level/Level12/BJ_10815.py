import sys


# list 자체 in 비교의 시간복잡도가 O(n)이므로 순서가 상관없고 중복체크만 하는 경우 set으로 사용하는 경우 시간초과를 없앨 수 있다.
def solution():
    aCardNum = int(sys.stdin.readline().strip())
    aCardList = set(map(int, sys.stdin.readline().strip().split(' ')))
    bCardNum = int(sys.stdin.readline().strip())
    bCardList = list(map(int, sys.stdin.readline().strip().split(' ')))

    answerList = [0] * bCardNum
    for num in range(bCardNum):
        if bCardList[num] in aCardList:
            answerList[num] = 1

    for i in answerList:
        sys.stdout.write(str(i) + ' ')

    return


# binary search
def solution2():
    aCardNum = int(sys.stdin.readline().strip())
    aCardList = sorted(map(int, sys.stdin.readline().split(' ')))
    # print(aCardList)
    bCardNum = int(sys.stdin.readline().strip())
    bCardList = list(map(int, sys.stdin.readline().split(' ')))

    answerList = [0] * bCardNum

    def binary(start, end, target, arr):
        while end >= start:
            mid = (start + end) // 2
            if arr[mid] == target:
                return 1
            if arr[mid] > target:
                end = mid - 1
            else:
                start = mid+1
        return 0

    for i in range(bCardNum):
        answerList[i] = binary(0, aCardNum-1 , bCardList[i], aCardList)

    for i in answerList:
        sys.stdout.write(str(i)+' ')

    return


if __name__ == '__main__':
    # solution()
    solution2()
