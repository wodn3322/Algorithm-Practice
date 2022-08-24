import sys

def solution():
    peopleNum = int(sys.stdin.readline().strip())
    peopleList = list(map(int,sys.stdin.readline().strip().split(' ')))
    peopleList.sort()
    cumlativeList = [0]*peopleNum
    cumlativeList[0]=peopleList[0]
    for i in range(1,peopleNum):
        cumlativeList[i]+=(cumlativeList[i-1]+peopleList[i])

    sys.stdout.write(str(sum((cumlativeList)))+'\n')

    return


if __name__ == '__main__':
    solution()
