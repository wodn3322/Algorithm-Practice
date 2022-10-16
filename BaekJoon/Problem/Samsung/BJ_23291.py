import sys

answer = 0


def solution():
    global answer
    n, k = map(int, sys.stdin.readline().strip().split(' '))

    fishBowl = [list(map(int, sys.stdin.readline().strip().split(' ')))]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if max(fishBowl[0]) - min(fishBowl[0]) <= k:
        print(answer)
        return

    for _ in range(int(n ** (1 / 2))):
        fishBowl.append([])

    def checkMin():
        minNum = min(fishBowl[0])
        for i in range(n):
            if fishBowl[0][i] == minNum:
                fishBowl[0][i] += 1

    def stackBowl():
        height = 1
        col = 0
        while height < len(fishBowl[0][height - 1:]):
            if height % 2 == 1:
                col += 1
            stackList = [[] for _ in range(col)]
            loopCheck = col
            if height % 2 == 0:
                loopCheck += 1
            for i in range(col):
                for j in range(loopCheck):
                    stackList[i].append(fishBowl[j][i])
            height += 1

            for i in range(col + 1):
                if i == 0:
                    fishBowl[i] = fishBowl[i][col:]
                else:
                    fishBowl[i] = stackList[col - i]

    def checkFish():
        checkMap = []
        heightList = [0]*len(fishBowl[0])
        for f in fishBowl:
            checkMap.append([0] * len(f))
        for i in range(len(fishBowl)):
            for j in range(len(fishBowl[i])):
                heightList[j]+=1
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < len(fishBowl) and 0 <= y < len(fishBowl[x]):
                        if fishBowl[x][y] > fishBowl[i][j]:
                            checkMap[x][y] -= (fishBowl[x][y] - fishBowl[i][j]) // 5
                            checkMap[i][j] += (fishBowl[x][y] - fishBowl[i][j]) // 5
                        else:
                            checkMap[i][j] -= (fishBowl[i][j] - fishBowl[x][y]) // 5
                            checkMap[x][y] += (fishBowl[i][j] - fishBowl[x][y]) // 5
        for i in range(len(fishBowl)):
            for j in range(len(fishBowl[i])):
                fishBowl[i][j] += (checkMap[i][j] // 2)
        arr = []
        for i in range(len(heightList)):
            for j in range(heightList[i]):
                arr.append(fishBowl[j][i])
        return arr
        # for i in range(len(fishBowl)):
        #     if i == 0:
        #         fishBowl[i] = arr
        #     else:
        #         fishBowl[i] = []

    def rotate180(num):

        arr1 = [[0]*(len(fishBowl)//2) for _ in range(len(fishBowl))]
        arr2 = [[0]*(len(fishBowl[0])//2) for _ in range(len(fishBowl))]
        print(arr1)
        for i in range(len(fishBowl)):
            for j in range(len(fishBowl[0])//2):
                print(i,j)
                arr1[i][j]=fishBowl[len(fishBowl)-i-1][len(fishBowl[0])//2-j-1]
                arr2[i][j] = fishBowl[i][len(fishBowl[0])//2+j]
        temp = []
        for a in arr2:
            temp.append(a)
        for a in arr1:
            temp.append(a)
        return temp


    # while True:
    checkMin()
    print(fishBowl)
    stackBowl()
    fishBowl=checkFish()
    for f in fishBowl:
        print(f)
    fishBowl = rotate180(1)
    fishBowl = rotate180(2)
    for f in fishBowl:
        print(f)

    return


if __name__ == '__main__':
    solution()
